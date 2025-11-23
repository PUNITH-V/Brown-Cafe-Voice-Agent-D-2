# ☕ Brown Cafe Agent

<div align="center">

![Brown Cafe](https://img.shields.io/badge/Brown_Cafe-AI_Voice_Agent-8b7355?style=for-the-badge)
![LiveKit](https://img.shields.io/badge/LiveKit-Agents-00A3E0?style=for-the-badge)
![Murf AI](https://img.shields.io/badge/Murf-Falcon_TTS-FF6B6B?style=for-the-badge)
![Next.js](https://img.shields.io/badge/Next.js-15-black?style=for-the-badge&logo=next.js)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python)

**An AI-Powered Voice Coffee Ordering System with Minimalist Design**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack) • [License](#-license)

</div>

---

## 🎯 Overview

Brown Cafe Agent is a sophisticated voice-activated coffee ordering application that combines cutting-edge AI technology with a refined minimalist aesthetic. Built for the **Murf AI Voice Agent Challenge**, this project demonstrates the seamless integration of natural language processing, real-time visualization, and elegant user experience design.

Transform the traditional coffee ordering experience into an intuitive voice conversation where customers simply speak their order naturally, and the AI barista intelligently collects all necessary details while providing real-time visual feedback.

## ✨ Features

### 🎙️ Voice-First Ordering
- **Natural Conversation Flow** - Speak naturally without rigid commands or scripts
- **Intelligent Context Understanding** - AI comprehends variations in how customers express preferences
- **Smart Clarification** - Automatically asks follow-up questions for missing information
- **Multi-Language Support** - Powered by Deepgram Nova-3 for accurate speech recognition

### 📊 Real-Time Visual Feedback
- **Live Order Visualization** - Watch your drink being built as you speak
- **Dynamic Cup Rendering** - Visual representation updates instantly with each order detail
- **Animated Barista Avatar** - Speaking animations provide natural interaction cues
- **Order Status Tracking** - Clear visual indicators of order completion progress

### 📝 Comprehensive Order Management
- **Complete Order Collection** - Drink type, size, milk preference, extras, and customer name
- **JSON Order Persistence** - All orders saved with timestamps for record-keeping
- **Professional Receipt Generation** - Beautifully formatted digital receipts
- **Order History** - Persistent storage of all completed orders

### 🎨 Minimalist Design Philosophy
- **Brown & Grey Color Palette** - Sophisticated earth tones (#8b7355, #2a2522, #6b5d52)
- **Clean Typography** - Light weights with generous letter spacing for modern elegance
- **Subtle Animations** - Smooth transitions without overwhelming the user
- **Responsive Layout** - Seamless experience across desktop and mobile devices

## 🎬 Demo

### Welcome Screen
Clean, minimalist landing page with elegant brown/grey theme

### Voice Ordering
Real-time drink visualization as you speak your order

### Order Receipt
Professional digital receipt with order confirmation

## 🛠️ Tech Stack

### Backend
- **LiveKit Agents Framework** - Real-time voice agent orchestration
- **Google Gemini 2.5 Flash** - Advanced LLM for natural conversation
- **Murf Falcon TTS** - High-quality text-to-speech (Matthew voice, Conversation style)
- **Deepgram Nova-3** - State-of-the-art speech-to-text recognition
- **Silero VAD** - Voice activity detection for turn management
- **Python 3.11+** - Modern Python with async/await patterns

### Frontend
- **Next.js 15** - React framework with App Router
- **TypeScript** - Type-safe development
- **LiveKit Client SDK** - Real-time audio/video communication
- **Framer Motion** - Smooth animations and transitions
- **Tailwind CSS** - Utility-first styling with custom brown/grey theme
- **DiceBear API** - Dynamic avatar generation

### Infrastructure
- **LiveKit Server** - Self-hosted WebRTC infrastructure
- **Real-time Data Channels** - Instant visualization updates
- **Noise Cancellation** - BVC (Background Voice Cancellation) for clear audio

## 📦 Installation

### Prerequisites
- Python 3.11 or higher
- Node.js 18 or higher
- pnpm (or npm/yarn)
- LiveKit Server
- API Keys:
  - Google Gemini API Key
  - Murf API Key
  - Deepgram API Key
  - LiveKit API Key and Secret

### 1. Clone the Repository
```bash
git clone https://github.com/PUNITH-V/Brown-Cafe-Voice-Agent-D-2.git
cd Brown-Cafe-Voice-Agent-D-2
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
copy .env.example .env.local
# Edit .env.local with your API keys
```

**Backend `.env.local` Configuration:**
```env
LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
GOOGLE_API_KEY=your_google_gemini_api_key
MURF_API_KEY=your_murf_api_key
DEEPGRAM_API_KEY=your_deepgram_api_key
```

### 3. Frontend Setup

```bash
cd ../frontend

# Install dependencies
pnpm install

# Configure environment variables
copy .env.example .env.local
# Edit .env.local with your LiveKit URL
```

**Frontend `.env.local` Configuration:**
```env
NEXT_PUBLIC_LIVEKIT_URL=ws://localhost:7880
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
```

### 4. LiveKit Server Setup

Download and run LiveKit Server:
```bash
# Download from https://github.com/livekit/livekit/releases
# Or use the provided setup in C:\LiveKit\

# Run LiveKit Server
livekit-server --dev
```

## 🚀 Usage

### Option 1: Use the Startup Script (Windows)
```bash
# From the project root
start-all.bat
```

This will automatically start:
1. LiveKit Server
2. Backend Agent
3. Frontend Application

### Option 2: Manual Start

**Terminal 1 - LiveKit Server:**
```bash
cd C:\LiveKit
livekit-server --dev
```

**Terminal 2 - Backend Agent:**
```bash
cd backend
.venv\Scripts\activate
python -m livekit.agents start
```

**Terminal 3 - Frontend:**
```bash
cd frontend
pnpm dev
```

### Access the Application
Open your browser and navigate to: `http://localhost:3000`

## 🎯 How to Order

1. **Click "Start Ordering"** on the welcome screen
2. **Speak your order naturally**, for example:
   - "I'd like a large latte with oat milk"
   - "Can I get a medium cappuccino with an extra shot?"
   - "I want a small mocha with whipped cream"
3. **Watch the visualization** update in real-time
4. **Provide your name** when asked
5. **Receive your digital receipt** when the order is complete

## 📊 Order Data Structure

Orders are saved as JSON files in `backend/orders/`:

```json
{
  "drinkType": "latte",
  "size": "medium",
  "milk": "oat milk",
  "extras": ["extra shot", "caramel drizzle"],
  "name": "Alex",
  "timestamp": "2025-11-23T14:46:38.123456",
  "status": "completed"
}
```

## 🎨 Design System

### Color Palette
```css
Primary Brown:   #8b7355
Dark Brown:      #6b5d52
Light Brown:     #a89584
Dark Grey:       #2a2522, #1a1816
Medium Grey:     #3a3330
Background:      linear-gradient(135deg, #2a2522, #1a1816)
```

### Typography
- **Font Family**: Inter, -apple-system, sans-serif
- **Weights**: 300 (Light), 400 (Regular)
- **Letter Spacing**: 0.2em - 0.4em for uppercase text
- **Text Transform**: Uppercase for headers and labels

## 🔧 Configuration

### Available Drinks
- Latte
- Cappuccino
- Espresso
- Americano
- Mocha
- Cold Brew

### Sizes
- Small
- Medium
- Large

### Milk Options
- Whole Milk
- Skim Milk
- Oat Milk
- Almond Milk
- Soy Milk
- No Milk

### Extras
- Extra Shot
- Whipped Cream
- Caramel Drizzle
- Vanilla Syrup

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Murf AI** - For the amazing Falcon TTS voice synthesis
- **LiveKit** - For the robust real-time communication framework
- **Google** - For Gemini 2.5 Flash LLM
- **Deepgram** - For accurate speech recognition
- **Next.js Team** - For the excellent React framework

## 📧 Contact

**PUNITH-V**
- GitHub: [@PUNITH-V](https://github.com/PUNITH-V)
- Email: punithvuppu@gmail.com

## 🌟 Show Your Support

If you found this project helpful, please give it a ⭐️!

---

<div align="center">

**Built with ❤️ for the Murf AI Voice Agent Challenge**

[⬆ Back to Top](#-brown-cafe-agent)

</div>
