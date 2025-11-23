import logging
import json
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    MetricsCollectedEvent,
    RoomInputOptions,
    WorkerOptions,
    cli,
    metrics,
    tokenize,
    function_tool,
    RunContext
)
from livekit import rtc
from livekit.plugins import murf, silero, google, deepgram, noise_cancellation
from livekit.plugins.turn_detector.multilingual import MultilingualModel

logger = logging.getLogger("agent")

# Load environment variables from .env.local first, then .env as fallback

load_dotenv(".env")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""You are a friendly and enthusiastic barista at Brown Cafe. The user is interacting with you via voice.
            Your job is to take coffee orders and ensure all order details are complete.
            
            IMPORTANT: You MUST use the provided tools to update the order:
            - When customer mentions a drink, IMMEDIATELY call update_drink_type tool
            - When customer mentions size, IMMEDIATELY call update_size tool
            - When customer mentions milk, IMMEDIATELY call update_milk tool
            - When customer mentions extras, IMMEDIATELY call add_extra tool
            - When customer provides their name, IMMEDIATELY call update_name tool
            - When all information is collected, call save_order tool
            
            You need to collect:
            1. Drink type (latte, cappuccino, espresso, americano, mocha, cold brew)
            2. Size (small, medium, large)
            3. Milk type (whole milk, skim milk, oat milk, almond milk, soy milk, no milk)
            4. Extras (extra shot, whipped cream, caramel drizzle, vanilla syrup)
            5. Customer name
            
            Be conversational and friendly. Ask clarifying questions one at a time if information is missing.
            Keep your responses natural and concise without complex formatting, emojis, or asterisks.""",
        )
        
        # Initialize order state
        self.order_state = {
            "drinkType": None,
            "size": None,
            "milk": None,
            "extras": [],
            "name": None
        }
        
        # Store room reference for sending data
        self.room = None
    
    def generate_drink_html(self):
        """Generate HTML visualization of the current drink order"""
        
        # Determine cup size - smaller to prevent overlap
        size_config = {
            "small": {"height": "80px", "width": "60px"},
            "medium": {"height": "95px", "width": "70px"},
            "large": {"height": "110px", "width": "80px"}
        }
        cup_size = size_config.get(self.order_state["size"], size_config["medium"])
        
        # Determine drink color based on type
        drink_colors = {
            "latte": "#D4A574",
            "cappuccino": "#A67C52",
            "espresso": "#4A2C2A",
            "americano": "#5D4037",
            "mocha": "#7B4B3A",
            "cold brew": "#6D4C41"
        }
        drink_color = drink_colors.get(self.order_state["drinkType"], "#A67C52")
        
        # Check for whipped cream
        has_whipped_cream = any("whipped cream" in extra.lower() for extra in self.order_state["extras"])
        
        # Build extras list
        extras_html = ""
        if self.order_state["extras"]:
            extras_items = "".join([f"<div style='margin: 2px 0; font-size: 12px;'>• {extra}</div>" for extra in self.order_state["extras"]])
            extras_html = f'<div style="margin: 0;">{extras_items}</div>'
        
        html = f"""
        <div style="font-family: 'Inter', -apple-system, sans-serif; padding: 16px; background: linear-gradient(135deg, #3a3330 0%, #2a2522 100%); border-radius: 2px; max-width: 280px; margin: 0 auto; color: #a89584; box-shadow: 0 8px 32px rgba(0,0,0,0.4); border: 1px solid #8b7355/20;">
            <div style="text-align: center; margin-bottom: 12px; padding-bottom: 12px; border-bottom: 1px solid #8b7355/20;">
                <h2 style="margin: 0; font-size: 14px; font-weight: 300; letter-spacing: 0.3em; text-transform: uppercase; color: #8b7355;">
                    <span style="font-size: 16px; margin-right: 8px;">☕</span>
                    <span>Brown Cafe</span>
                </h2>
            </div>
            
            <div style="background: #1a1816; border-radius: 2px; padding: 14px; color: #a89584; border: 1px solid #8b7355/10;">
                <h3 style="margin: 0 0 12px 0; color: #8b7355; text-align: center; font-size: 12px; font-weight: 300; letter-spacing: 0.2em; text-transform: uppercase; padding-bottom: 8px; border-bottom: 1px solid #8b7355/20;">Your Order</h3>
                
                <!-- Drink Visualization -->
                <div style="display: flex; justify-content: center; align-items: center; margin: 12px 0; padding: 16px; background: #2a2522; border-radius: 2px; border: 1px solid #8b7355/10;">
                    <div style="position: relative; display: inline-block;">
                        <!-- Minimalist Cup -->
                        <div style="position: relative; width: {cup_size['width']}; height: {cup_size['height']}; background: linear-gradient(to bottom, {drink_color} 0%, {drink_color} 85%, #3e2723 100%); border-radius: 0 0 12px 12px; box-shadow: 0 4px 16px rgba(0,0,0,0.3), inset -3px 0 8px rgba(0,0,0,0.2), inset 3px 0 8px rgba(255,255,255,0.1); border: 2px solid #3e2723; border-top: none;">
                            <!-- Cup Top/Rim -->
                            <div style="position: absolute; top: -6px; left: -2px; right: -2px; height: 10px; background: {drink_color}; border: 2px solid #3e2723; border-radius: 50%; box-shadow: inset 0 -2px 4px rgba(0,0,0,0.3);"></div>
                            
                            <!-- Whipped Cream -->
                            {f'''<div style="position: absolute; top: -22px; left: 50%; transform: translateX(-50%); width: calc(100% - 8px); height: 30px; background: radial-gradient(ellipse at center, #FFFEF7 0%, #FFF8E7 50%, #F5E6D3 100%); border-radius: 50% 50% 40% 40%; box-shadow: 0 2px 6px rgba(0,0,0,0.2); border: 1px solid #F0E5D8;"></div>
                            <div style="position: absolute; top: -26px; left: 50%; transform: translateX(-50%); width: 55%; height: 18px; background: radial-gradient(circle, #FFFFFF 0%, #FFFEF7 100%); border-radius: 50%; opacity: 0.9;"></div>''' if has_whipped_cream else ''}
                            
                            <!-- Cup Handle -->
                            <div style="position: absolute; right: -20px; top: 25%; width: 24px; height: 40%; border: 3px solid #3e2723; border-left: none; border-radius: 0 50% 50% 0; background: linear-gradient(to right, transparent 0%, {drink_color} 50%); opacity: 0.7;"></div>
                        </div>
                        
                        <!-- Size Badge -->
                        <div style="text-align: center; margin-top: 10px;">
                            <span style="display: inline-block; background: #8b7355; color: #1a1816; padding: 4px 12px; border-radius: 1px; font-weight: 300; font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase; box-shadow: 0 2px 8px rgba(0,0,0,0.2);">
                                {self.order_state["size"].upper() if self.order_state["size"] else "SIZE"}
                            </span>
                        </div>
                    </div>
                </div>
                
                <!-- Order Details -->
                <div style="margin-top: 12px; background: #2a2522; border-radius: 2px; padding: 10px; font-size: 11px; border: 1px solid #8b7355/10;">
                    <div style="display: grid; grid-template-columns: auto 1fr; gap: 6px 12px; align-items: start;">
                        <strong style="color: #8b7355; font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase; font-size: 10px;">Drink:</strong>
                        <span style="color: #a89584;">{self.order_state["drinkType"] or "—"}</span>
                        
                        <strong style="color: #8b7355; font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase; font-size: 10px;">Size:</strong>
                        <span style="color: #a89584;">{self.order_state["size"] or "—"}</span>
                        
                        <strong style="color: #8b7355; font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase; font-size: 10px;">Milk:</strong>
                        <span style="color: #a89584;">{self.order_state["milk"] or "—"}</span>
                        
                        <strong style="color: #8b7355; font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase; font-size: 10px;">Extras:</strong>
                        <div style="color: #a89584;">{extras_html if self.order_state["extras"] else '<span style="color: #6b5d52; font-size: 10px;">—</span>'}</div>
                        
                        <strong style="color: #8b7355; font-weight: 300; letter-spacing: 0.1em; text-transform: uppercase; font-size: 10px;">Name:</strong>
                        <span style="color: #a89584;">{self.order_state["name"] or "—"}</span>
                    </div>
                </div>
            </div>
        </div>
        """
        
        return html
    
    async def send_drink_visualization(self):
        """Send the drink visualization HTML to the frontend"""
        if self.room:
            try:
                html = self.generate_drink_html()
                # Send as data message
                await self.room.local_participant.publish_data(
                    html.encode('utf-8'),
                    topic="drink_visualization"
                )
                logger.info("Sent drink visualization to frontend")
            except Exception as e:
                logger.error(f"Failed to send visualization: {e}")
    
    def generate_receipt_html(self):
        """Generate HTML receipt for completed order"""
        extras_list = ", ".join(self.order_state["extras"]) if self.order_state["extras"] else "None"
        order_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        
        html = f"""
        <div style="font-family: 'Inter', -apple-system, sans-serif; padding: 24px; background: #f5f3f0; border-radius: 2px; max-width: 380px; margin: 0 auto; color: #3a3330; box-shadow: 0 12px 48px rgba(0,0,0,0.2); border: 1px solid #8b7355/20;">
            <div style="text-align: center; border-bottom: 1px solid #8b7355/20; padding-bottom: 18px; margin-bottom: 18px;">
                <div style="font-size: 28px; margin-bottom: 10px; opacity: 0.8;">☕</div>
                <h2 style="margin: 0; font-size: 18px; font-weight: 300; letter-spacing: 0.3em; color: #8b7355; text-transform: uppercase;">Brown Cafe</h2>
                <p style="margin: 6px 0 0 0; font-size: 11px; color: #6b5d52; letter-spacing: 0.2em; text-transform: uppercase;">Order Receipt</p>
            </div>
            
            <div style="margin-bottom: 18px;">
                <p style="margin: 6px 0; font-size: 12px; color: #6b5d52;"><strong style="font-weight: 400; color: #8b7355;">Order #:</strong> {datetime.now().strftime('%Y%m%d%H%M%S')}</p>
                <p style="margin: 6px 0; font-size: 12px; color: #6b5d52;"><strong style="font-weight: 400; color: #8b7355;">Date:</strong> {order_time}</p>
                <p style="margin: 6px 0; font-size: 12px; color: #6b5d52;"><strong style="font-weight: 400; color: #8b7355;">Customer:</strong> {self.order_state["name"]}</p>
            </div>
            
            <div style="border-top: 1px solid #8b7355/20; border-bottom: 1px solid #8b7355/20; padding: 14px 0; margin: 18px 0;">
                <p style="margin: 10px 0; font-size: 13px; color: #3a3330;"><strong style="font-weight: 400; color: #8b7355;">ITEM:</strong> {self.order_state["drinkType"].title()}</p>
                <p style="margin: 10px 0; font-size: 13px; padding-left: 20px; color: #6b5d52;">Size: {self.order_state["size"].title()}</p>
                <p style="margin: 10px 0; font-size: 13px; padding-left: 20px; color: #6b5d52;">Milk: {self.order_state["milk"]}</p>
                <p style="margin: 10px 0; font-size: 13px; padding-left: 20px; color: #6b5d52;">Extras: {extras_list}</p>
            </div>
            
            <div style="text-align: center; margin-top: 18px; padding-top: 18px; border-top: 1px solid #8b7355/20;">
                <p style="margin: 10px 0; font-size: 16px; font-weight: 300; color: #8b7355; letter-spacing: 0.2em; text-transform: uppercase;">✓ Confirmed</p>
                <p style="margin: 10px 0; font-size: 12px; color: #6b5d52;">Your order will be ready shortly</p>
            </div>
            
            <div style="text-align: center; margin-top: 18px; padding-top: 14px; border-top: 1px solid #8b7355/10;">
                <p style="margin: 5px 0; font-size: 10px; color: #6b5d52/60; letter-spacing: 0.1em;">Thank you for choosing Brown Cafe</p>
                <p style="margin: 5px 0; font-size: 10px; color: #6b5d52/60; letter-spacing: 0.1em;">Powered by Murf Falcon TTS</p>
            </div>
        </div>
        """
        return html
    
    async def send_receipt(self):
        """Send the receipt HTML to the frontend"""
        if self.room:
            try:
                html = self.generate_receipt_html()
                # Send as data message
                await self.room.local_participant.publish_data(
                    html.encode('utf-8'),
                    topic="order_receipt"
                )
                logger.info("Sent order receipt to frontend")
            except Exception as e:
                logger.error(f"Failed to send receipt: {e}")

    @function_tool
    async def save_order(self, context: RunContext):
        """Use this tool when all order information is collected (drinkType, size, milk, extras, and name).
        This will save the complete order to a JSON file.
        """
        
        # Check if all required fields are filled
        if not all([
            self.order_state["drinkType"],
            self.order_state["size"],
            self.order_state["milk"] is not None,
            self.order_state["name"]
        ]):
            return "Order is incomplete. Please collect all required information first."
        
        # Create orders directory if it doesn't exist
        orders_dir = Path("orders")
        orders_dir.mkdir(exist_ok=True)
        
        # Add timestamp to order
        order_with_timestamp = {
            **self.order_state,
            "timestamp": datetime.now().isoformat(),
            "status": "completed"
        }
        
        # Generate filename with timestamp
        filename = f"order_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{self.order_state['name'].replace(' ', '_')}.json"
        filepath = orders_dir / filename
        
        # Save to JSON file
        with open(filepath, 'w') as f:
            json.dump(order_with_timestamp, f, indent=2)
        
        logger.info(f"Order saved to {filepath}")
        logger.info(f"Order details: {json.dumps(order_with_timestamp, indent=2)}")
        
        # Generate and send receipt
        await self.send_receipt()
        
        # Reset order state for next customer
        self.order_state = {
            "drinkType": None,
            "size": None,
            "milk": None,
            "extras": [],
            "name": None
        }
        
        return f"Order saved successfully! Your order will be ready soon."
    
    @function_tool
    async def update_drink_type(self, context: RunContext, drink_type: str):
        """Update the drink type in the order.
        
        Args:
            drink_type: The type of drink (e.g., latte, cappuccino, espresso, americano, mocha, cold brew)
        """
        self.order_state["drinkType"] = drink_type
        logger.info(f"Updated drink type: {drink_type}")
        await self.send_drink_visualization()
        return f"Got it, {drink_type}."
    
    @function_tool
    async def update_size(self, context: RunContext, size: str):
        """Update the size in the order.
        
        Args:
            size: The size of the drink (small, medium, or large)
        """
        self.order_state["size"] = size.lower()
        logger.info(f"Updated size: {size}")
        await self.send_drink_visualization()
        return f"Perfect, {size} size."
    
    @function_tool
    async def update_milk(self, context: RunContext, milk_type: str):
        """Update the milk type in the order.
        
        Args:
            milk_type: The type of milk (whole milk, skim milk, oat milk, almond milk, soy milk, or no milk)
        """
        self.order_state["milk"] = milk_type
        logger.info(f"Updated milk: {milk_type}")
        await self.send_drink_visualization()
        return f"Noted, {milk_type}."
    
    @function_tool
    async def add_extra(self, context: RunContext, extra: str):
        """Add an extra item to the order.
        
        Args:
            extra: An extra item (e.g., extra shot, whipped cream, caramel drizzle, vanilla syrup)
        """
        if extra not in self.order_state["extras"]:
            self.order_state["extras"].append(extra)
        logger.info(f"Added extra: {extra}")
        await self.send_drink_visualization()
        return f"Added {extra}."
    
    @function_tool
    async def update_name(self, context: RunContext, customer_name: str):
        """Update the customer name for the order.
        
        Args:
            customer_name: The customer's name
        """
        self.order_state["name"] = customer_name
        logger.info(f"Updated name: {customer_name}")
        await self.send_drink_visualization()
        return f"Great, {customer_name}."
    
    @function_tool
    async def check_order_status(self, context: RunContext):
        """Check what information is still needed for the order."""
        missing = []
        if not self.order_state["drinkType"]:
            missing.append("drink type")
        if not self.order_state["size"]:
            missing.append("size")
        if self.order_state["milk"] is None:
            missing.append("milk preference")
        if not self.order_state["name"]:
            missing.append("name")
        
        if missing:
            return f"Still need: {', '.join(missing)}"
        else:
            return f"Order complete: {json.dumps(self.order_state, indent=2)}"


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    # Logging setup
    # Add any other context you want in all log entries here
    ctx.log_context_fields = {
        "room": ctx.room.name,
    }

    # Set up a voice AI pipeline using OpenAI, Cartesia, AssemblyAI, and the LiveKit turn detector
    session = AgentSession(
        # Speech-to-text (STT) is your agent's ears, turning the user's speech into text that the LLM can understand
        # See all available models at https://docs.livekit.io/agents/models/stt/
        stt=deepgram.STT(model="nova-3"),
        # A Large Language Model (LLM) is your agent's brain, processing user input and generating a response
        # See all available models at https://docs.livekit.io/agents/models/llm/
        llm=google.LLM(
                model="gemini-2.5-flash",
            ),
        # Text-to-speech (TTS) is your agent's voice, turning the LLM's text into speech that the user can hear
        # See all available models as well as voice selections at https://docs.livekit.io/agents/models/tts/
        tts=murf.TTS(
                voice="en-US-matthew", 
                style="Conversation",
                tokenizer=tokenize.basic.SentenceTokenizer(min_sentence_len=2),
                text_pacing=True
            ),
        # VAD and turn detection are used to determine when the user is speaking and when the agent should respond
        # See more at https://docs.livekit.io/agents/build/turns
        turn_detection=MultilingualModel(),
        vad=ctx.proc.userdata["vad"],
        # allow the LLM to generate a response while waiting for the end of turn
        # See more at https://docs.livekit.io/agents/build/audio/#preemptive-generation
        preemptive_generation=True,
    )

    # To use a realtime model instead of a voice pipeline, use the following session setup instead.
    # (Note: This is for the OpenAI Realtime API. For other providers, see https://docs.livekit.io/agents/models/realtime/))
    # 1. Install livekit-agents[openai]
    # 2. Set OPENAI_API_KEY in .env.local
    # 3. Add `from livekit.plugins import openai` to the top of this file
    # 4. Use the following session setup instead of the version above
    # session = AgentSession(
    #     llm=openai.realtime.RealtimeModel(voice="marin")
    # )

    # Metrics collection, to measure pipeline performance
    # For more information, see https://docs.livekit.io/agents/build/metrics/
    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent):
        metrics.log_metrics(ev.metrics)
        usage_collector.collect(ev.metrics)

    async def log_usage():
        summary = usage_collector.get_summary()
        logger.info(f"Usage: {summary}")

    ctx.add_shutdown_callback(log_usage)

    # # Add a virtual avatar to the session, if desired
    # # For other providers, see https://docs.livekit.io/agents/models/avatar/
    # avatar = hedra.AvatarSession(
    #   avatar_id="...",  # See https://docs.livekit.io/agents/models/avatar/plugins/hedra
    # )
    # # Start the avatar and wait for it to join
    # await avatar.start(session, room=ctx.room)

    # Create assistant and set room reference
    assistant = Assistant()
    assistant.room = ctx.room
    
    # Start the session, which initializes the voice pipeline and warms up the models
    await session.start(
        agent=assistant,
        room=ctx.room,
        room_input_options=RoomInputOptions(
            # For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    # Join the room and connect to the user
    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
