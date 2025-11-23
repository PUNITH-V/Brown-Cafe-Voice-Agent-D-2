# ☕ Murf Coffee Shop - AI Voice Barista

A real-time AI voice coffee ordering system built with LiveKit Agents, Murf Falcon TTS, Google Gemini, and Deepgram STT.

> **Part of the Murf AI Voice Agents Challenge - Day 2**

[![GitHub](https://img.shields.io/badge/GitHub-Voice--Agents--Day2-blue?logo=github)](https://github.com/Gangadhar-NG-CODER/Voice-Agents-Day2)
[![LiveKit](https://img.shields.io/badge/Built%20with-LiveKit-00ADD8?logo=livekit)](https://livekit.io/)
[![Murf](https://img.shields.io/badge/Powered%20by-Murf%20Falcon-orange)](https://murf.ai/)

## ✨ Features

### Coffee Ordering
- 🎙️ **Voice Ordering** - Natural conversation-based coffee ordering
- 📊 **Real-time Visualization** - Live order display with dynamic cup rendering
- 🧾 **Automated Receipts** - Professional receipt generation after order completion
- 🔄 **Order State Management** - Tracks drink type, size, milk, extras, and customer name
- ✅ **Smart Validation** - Ensures all order details are collected before saving

### Technical Features
- ⚡ **Ultra-fast TTS** - Powered by Murf Falcon (fastest TTS API)
- 🧠 **Intelligent AI** - Google Gemini 2.5 Flash for natural conversations
- 🎯 **Accurate STT** - Deepgram Nova-3 for speech recognition
- 🎨 **Modern Dark UI** - Sleek coffee shop themed interface
- 💾 **Order Persistence** - Saves orders to JSON files with timestamps

## Tech Stack

**Backend:**
- Python 3.9+
- LiveKit Agents
- Murf Falcon TTS
- Google Gemini LLM
- Deepgram STT
- Silero VAD

**Frontend:**
- Next.js 15
- React 19
- TypeScript
- Tailwind CSS
- LiveKit Client SDK

## Prerequisites

- Python 3.9+ with [uv](https://docs.astral.sh/uv/) package manager
- Node.js 18+ with pnpm
- LiveKit Server (for local development)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Gangadhar-NG-CODER/Voice-Agents-Day2.git
cd Voice-Agents-Day2
```

### 2. Install uv (Python Package Manager)

```bash
pip install uv
```

### 3. Install pnpm (Node Package Manager)

```bash
npm install -g pnpm
```

### 4. Backend Setup

```bash
cd backend

# Install dependencies
uv sync

# Copy environment file
cp .env.example .env.local

# Edit .env.local with your API keys:
# - LIVEKIT_URL=ws://127.0.0.1:7880
# - LIVEKIT_API_KEY=devkey
# - LIVEKIT_API_SECRET=secret
# - GOOGLE_API_KEY=your_google_api_key
# - MURF_API_KEY=your_murf_api_key
# - DEEPGRAM_API_KEY=your_deepgram_api_key

# Download required models
uv run python src/agent.py download-files
```

### 5. Frontend Setup

```bash
cd frontend

# Install dependencies
pnpm install

# Copy environment file
cp .env.example .env.local

# Edit .env.local with LiveKit credentials
```

### 6. Download LiveKit Server

Download LiveKit server from [LiveKit Releases](https://github.com/livekit/livekit/releases) and place it in a convenient location.

## Running the Application

You need to run three services in separate terminals:

### Terminal 1 - LiveKit Server

```bash
# Navigate to where you downloaded livekit-server
livekit-server.exe --dev
```

### Terminal 2 - Backend Agent

```bash
cd backend

# First time: Copy the example file
copy run.bat.example run.bat
# Edit run.bat and add your API keys

# Then run:
.\run.bat
```

### Terminal 3 - Frontend

```bash
cd frontend
pnpm dev
```

Then open **http://localhost:3000** in your browser!

## API Keys

You'll need API keys from:

- **Google AI Studio**: [Get API Key](https://aistudio.google.com/apikey)
- **Murf.ai**: [Get API Key](https://murf.ai/api)
- **Deepgram**: [Get API Key](https://deepgram.com/)

## Project Structure

```
Voice-Agents/
├── backend/          # Python backend with LiveKit Agents
│   ├── src/
│   │   └── agent.py  # Main agent logic
│   ├── .env.local    # Environment variables
│   └── run.bat       # Windows startup script
├── frontend/         # Next.js frontend
│   ├── app/          # Next.js app directory
│   ├── components/   # React components
│   └── .env.local    # Frontend environment variables
└── README.md
```

## Customization

### Modify Agent Personality

Edit `backend/src/agent.py` and update the `instructions` in the `Assistant` class:

```python
class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="Your custom instructions here...",
        )
```

### Change Voice

Modify the TTS configuration in `backend/src/agent.py`:

```python
tts=murf.TTS(
    voice="en-US-matthew",  # Change voice here
    style="Conversation",
    tokenizer=tokenize.basic.SentenceTokenizer(min_sentence_len=2),
    text_pacing=True
)
```

## Troubleshooting

### Backend won't connect to LiveKit

Make sure:
1. LiveKit server is running on port 7880
2. Environment variables are set correctly in `.env.local`
3. Use the `run.bat` script to ensure environment variables are loaded

### Frontend connection issues

Check that:
1. `.env.local` has the correct `LIVEKIT_URL=ws://127.0.0.1:7880`
2. All three services are running
3. No firewall is blocking the connections

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details

## Acknowledgments

- Built with [LiveKit](https://livekit.io/)
- Powered by [Murf Falcon TTS](https://murf.ai/)
- Based on LiveKit's agent starter templates

## Author

**Gangadhar NG**
- GitHub: [@Gangadhar-NG-CODER](https://github.com/Gangadhar-NG-CODER)
- Repository: [Voice-Agents-Day2](https://github.com/Gangadhar-NG-CODER/Voice-Agents-Day2)

---

⭐ Star this repo if you find it helpful!

## Live Demo

Check out the demo video on LinkedIn: [#MurfAIVoiceAgentsChallenge](https://www.linkedin.com/feed/hashtag/murfaivoiceagentschallenge/)
