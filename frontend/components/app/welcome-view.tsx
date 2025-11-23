import { Button } from '@/components/livekit/button';

function MinimalLine() {
  return (
    <div className="w-16 h-px bg-gradient-to-r from-transparent via-[#8b7355] to-transparent mb-8 opacity-40"></div>
  );
}

function CoffeeIcon() {
  return (
    <div className="relative mb-12">
      {/* Minimal circle frame */}
      <div className="absolute inset-0 -m-6 border border-[#8b7355]/20 rounded-full"></div>
      
      {/* Subtle glow */}
      <div className="absolute inset-0 blur-2xl opacity-20 bg-[#8b7355] animate-pulse-slow"></div>
      
      {/* Main coffee cup */}
      <div className="relative">
        <div className="text-7xl filter drop-shadow-lg">☕</div>
      </div>
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
    <div ref={ref} className="min-h-screen bg-gradient-to-br from-[#2a2522] via-[#1a1816] to-[#2a2522] relative overflow-hidden">
      {/* Minimalist Grid Pattern */}
      <div className="absolute inset-0 opacity-[0.03]" style={{
        backgroundImage: `linear-gradient(#8b7355 1px, transparent 1px), linear-gradient(90deg, #8b7355 1px, transparent 1px)`,
        backgroundSize: '50px 50px'
      }}></div>
      
      {/* Subtle Accent Lines */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-0 left-1/2 w-px h-full bg-gradient-to-b from-transparent via-[#8b7355]/10 to-transparent"></div>
        <div className="absolute top-1/2 left-0 w-full h-px bg-gradient-to-r from-transparent via-[#8b7355]/10 to-transparent"></div>
      </div>
      
      {/* Minimal Floating Elements */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-20 left-10 text-5xl opacity-5 animate-float text-[#8b7355]">☕</div>
        <div className="absolute bottom-32 right-20 text-5xl opacity-5 animate-float-delayed text-[#8b7355]">☕</div>
        
        {/* Subtle glow effects */}
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-[#8b7355]/5 rounded-full blur-3xl animate-pulse-slow"></div>
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-[#6b5d52]/5 rounded-full blur-3xl animate-pulse-slow" style={{animationDelay: '2s'}}></div>
      </div>

      <section className="relative z-10 flex flex-col items-center justify-center text-center min-h-screen px-4">
        {/* Minimal line top */}
        <MinimalLine />
        
        {/* Logo/Icon */}
        <CoffeeIcon />

        {/* Title - Minimalist */}
        <h1 className="text-6xl md:text-7xl font-light tracking-[0.3em] text-[#8b7355] mb-3 animate-fade-in uppercase">
          BROWN CAFE
        </h1>
        
        <h2 className="text-sm md:text-base font-light text-[#6b5d52]/60 mb-12 animate-fade-in-delay tracking-[0.4em] uppercase">
          Est. 2025
        </h2>

        {/* Minimal line */}
        <div className="w-24 h-px bg-gradient-to-r from-transparent via-[#8b7355]/40 to-transparent mb-8"></div>

        {/* Subtitle - Clean */}
        <p className="text-lg md:text-xl text-[#a89584] mb-2 max-w-md leading-relaxed font-light tracking-wide animate-fade-in-delay">
          AI-Powered Coffee Ordering
        </p>

        {/* Description - Minimal */}
        <p className="text-sm md:text-base text-[#6b5d52]/50 mb-16 max-w-lg font-light animate-fade-in-delay-2">
          Voice • Precision • Simplicity
        </p>

        {/* Minimalist Start Button */}
        <Button 
          variant="primary" 
          size="lg" 
          onClick={onStartCall} 
          className="group relative mt-4 px-12 py-6 text-base font-light uppercase tracking-[0.3em] bg-[#8b7355] text-white hover:bg-[#6b5d52] transition-all duration-500 border border-[#8b7355]/30 hover:border-[#8b7355] shadow-lg hover:shadow-xl hover:scale-105 animate-fade-in-delay-3"
        >
          <span className="relative z-10 flex items-center gap-3">
            <span className="text-lg">○</span>
            <span>{startButtonText}</span>
          </span>
        </Button>
        
        {/* Tagline */}
        <p className="mt-8 text-[#6b5d52]/40 text-xs font-light tracking-widest animate-fade-in-delay-3 uppercase">
          Powered by AI
        </p>

        {/* Minimal Feature Cards */}
        <div className="mt-32 grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl animate-fade-in-delay-4">
          <div className="group relative bg-[#2a2522]/40 backdrop-blur-sm p-8 border border-[#8b7355]/10 hover:border-[#8b7355]/30 transition-all duration-500 hover:-translate-y-2">
            <div className="relative">
              <div className="text-4xl mb-4 opacity-60 group-hover:opacity-100 transition-opacity duration-500">🎙️</div>
              <h3 className="text-[#a89584] text-base font-light mb-2 tracking-wider uppercase">Voice</h3>
              <p className="text-[#6b5d52]/60 text-sm font-light">Natural conversation</p>
            </div>
          </div>
          
          <div className="group relative bg-[#2a2522]/40 backdrop-blur-sm p-8 border border-[#8b7355]/10 hover:border-[#8b7355]/30 transition-all duration-500 hover:-translate-y-2">
            <div className="relative">
              <div className="text-4xl mb-4 opacity-60 group-hover:opacity-100 transition-opacity duration-500">⚡</div>
              <h3 className="text-[#a89584] text-base font-light mb-2 tracking-wider uppercase">Speed</h3>
              <p className="text-[#6b5d52]/60 text-sm font-light">Instant response</p>
            </div>
          </div>
          
          <div className="group relative bg-[#2a2522]/40 backdrop-blur-sm p-8 border border-[#8b7355]/10 hover:border-[#8b7355]/30 transition-all duration-500 hover:-translate-y-2">
            <div className="relative">
              <div className="text-4xl mb-4 opacity-60 group-hover:opacity-100 transition-opacity duration-500">✨</div>
              <h3 className="text-[#a89584] text-base font-light mb-2 tracking-wider uppercase">Smart</h3>
              <p className="text-[#6b5d52]/60 text-sm font-light">Perfect understanding</p>
            </div>
          </div>
        </div>
        
        {/* Minimal bottom line */}
        <div className="mt-20 animate-fade-in-delay-4">
          <MinimalLine />
        </div>
      </section>

      {/* Minimal Footer */}
      <div className="fixed bottom-8 left-0 flex w-full items-center justify-center z-20">
        <p className="text-[#6b5d52]/40 text-xs font-light tracking-wider">
          LiveKit × Murf Falcon
        </p>
      </div>

      <style jsx>{`
        @keyframes float {
          0%, 100% { transform: translateY(0px) rotate(0deg); }
          50% { transform: translateY(-20px) rotate(5deg); }
        }
        @keyframes float-delayed {
          0%, 100% { transform: translateY(0px) rotate(0deg); }
          50% { transform: translateY(-15px) rotate(-5deg); }
        }
        @keyframes pulse-slow {
          0%, 100% { opacity: 0.2; transform: scale(1); }
          50% { opacity: 0.3; transform: scale(1.1); }
        }
        @keyframes spin-slow {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }
        @keyframes bounce-slow {
          0%, 100% { transform: translateY(0); }
          50% { transform: translateY(-10px); }
        }
        @keyframes fade-in {
          from { opacity: 0; transform: translateY(20px); }
          to { opacity: 1; transform: translateY(0); }
        }
        .animate-float {
          animation: float 6s ease-in-out infinite;
        }
        .animate-float-delayed {
          animation: float-delayed 8s ease-in-out infinite;
        }
        .animate-pulse-slow {
          animation: pulse-slow 4s ease-in-out infinite;
        }
        .animate-spin-slow {
          animation: spin-slow 8s linear infinite;
        }
        .animate-bounce-slow {
          animation: bounce-slow 3s ease-in-out infinite;
        }
        .animate-fade-in {
          animation: fade-in 0.8s ease-out forwards;
        }
        .animate-fade-in-delay {
          animation: fade-in 0.8s ease-out 0.2s forwards;
          opacity: 0;
        }
        .animate-fade-in-delay-2 {
          animation: fade-in 0.8s ease-out 0.4s forwards;
          opacity: 0;
        }
        .animate-fade-in-delay-3 {
          animation: fade-in 0.8s ease-out 0.6s forwards;
          opacity: 0;
        }
        .animate-fade-in-delay-4 {
          animation: fade-in 0.8s ease-out 0.8s forwards;
          opacity: 0;
        }
      `}</style>
    </div>
  );
};
