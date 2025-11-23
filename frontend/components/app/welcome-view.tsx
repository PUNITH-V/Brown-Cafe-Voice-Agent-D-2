import { Button } from '@/components/livekit/button';

function CoffeeIcon() {
  return (
    <div className="relative mb-8">
      <div className="text-8xl animate-bounce">☕</div>
      <div className="absolute -top-2 -right-2 text-4xl animate-pulse">✨</div>
    </div>
  );
}

interface WelcomeViewProps {
  startButtonText: string;
  onStartCall: () => void;
}

export const WelcomeView = ({
  startButtonText,
  onStartCall,
  ref,
}: React.ComponentProps<'div'> & WelcomeViewProps) => {
  return (
    <div ref={ref} className="min-h-screen bg-gradient-to-br from-gray-900 via-black to-gray-900 relative overflow-hidden">
      {/* Animated Background Elements */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-20 left-10 text-6xl opacity-5 animate-float">☕</div>
        <div className="absolute top-40 right-20 text-5xl opacity-5 animate-float-delayed">🥐</div>
        <div className="absolute bottom-32 left-1/4 text-7xl opacity-5 animate-float">🍰</div>
        <div className="absolute bottom-20 right-1/3 text-6xl opacity-5 animate-float-delayed">🧁</div>
        
        {/* Subtle glow effects */}
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-amber-600/10 rounded-full blur-3xl"></div>
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-orange-600/10 rounded-full blur-3xl"></div>
      </div>

      <section className="relative z-10 flex flex-col items-center justify-center text-center min-h-screen px-4">
        {/* Logo/Icon */}
        <CoffeeIcon />

        {/* Title */}
        <h1 className="text-5xl md:text-6xl font-bold text-white mb-4 drop-shadow-2xl">
          Murf Coffee Shop
        </h1>

        {/* Subtitle */}
        <p className="text-xl md:text-2xl text-amber-400 mb-3 max-w-2xl leading-relaxed font-medium">
          Your AI Barista is Ready to Take Your Order
        </p>

        {/* Description */}
        <p className="text-base md:text-lg text-gray-300 mb-10 max-w-xl">
          Order your favorite coffee with voice • Fast • Easy • Delicious
        </p>

        {/* Start Button */}
        <Button 
          variant="primary" 
          size="lg" 
          onClick={onStartCall} 
          className="mt-4 px-12 py-6 text-lg font-semibold bg-gradient-to-r from-amber-500 to-orange-500 text-black hover:from-amber-400 hover:to-orange-400 hover:scale-105 transition-all duration-300 shadow-2xl shadow-amber-500/50 rounded-full border-2 border-amber-400"
        >
          🎤 {startButtonText}
        </Button>

        {/* Features */}
        <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-6 max-w-4xl">
          <div className="bg-gray-800/50 backdrop-blur-sm rounded-2xl p-6 border-2 border-gray-700 shadow-lg hover:border-amber-500/50 transition-colors">
            <div className="text-4xl mb-3">🎙️</div>
            <h3 className="text-white font-semibold mb-2">Voice Ordering</h3>
            <p className="text-gray-400 text-sm">Just speak naturally to place your order</p>
          </div>
          <div className="bg-gray-800/50 backdrop-blur-sm rounded-2xl p-6 border-2 border-gray-700 shadow-lg hover:border-amber-500/50 transition-colors">
            <div className="text-4xl mb-3">⚡</div>
            <h3 className="text-white font-semibold mb-2">Lightning Fast</h3>
            <p className="text-gray-400 text-sm">Powered by Murf Falcon TTS</p>
          </div>
          <div className="bg-gray-800/50 backdrop-blur-sm rounded-2xl p-6 border-2 border-gray-700 shadow-lg hover:border-amber-500/50 transition-colors">
            <div className="text-4xl mb-3">✨</div>
            <h3 className="text-white font-semibold mb-2">Smart AI</h3>
            <p className="text-gray-400 text-sm">Understands your preferences perfectly</p>
          </div>
        </div>
      </section>

      {/* Footer */}
      <div className="fixed bottom-6 left-0 flex w-full items-center justify-center z-20">
        <p className="text-gray-400 text-sm font-medium">
          Built with ❤️ using LiveKit Agents & Murf Falcon
        </p>
      </div>

      <style jsx>{`
        @keyframes float {
          0%, 100% { transform: translateY(0px); }
          50% { transform: translateY(-20px); }
        }
        @keyframes float-delayed {
          0%, 100% { transform: translateY(0px); }
          50% { transform: translateY(-15px); }
        }
        .animate-float {
          animation: float 6s ease-in-out infinite;
        }
        .animate-float-delayed {
          animation: float-delayed 8s ease-in-out infinite;
        }
      `}</style>
    </div>
  );
};
