'use client';

import { useState, useEffect } from 'react';
import { useVoiceAssistant } from '@livekit/components-react';

export function BaristaAvatar() {
  const { state } = useVoiceAssistant();
  const [isSpeaking, setIsSpeaking] = useState(false);

  useEffect(() => {
    setIsSpeaking(state === 'speaking');
  }, [state]);

  return (
    <div className="fixed top-8 left-8 z-50">
      <div className="relative">
        {/* Glow effect when speaking */}
        {isSpeaking && (
          <div className="absolute inset-0 rounded-full bg-gradient-to-r from-amber-500 to-orange-500 blur-2xl opacity-60 animate-pulse"></div>
        )}
        
        {/* Avatar container */}
        <div className={`relative w-24 h-24 rounded-full border-4 transition-all duration-300 ${
          isSpeaking 
            ? 'border-amber-400 shadow-[0_0_30px_rgba(251,191,36,0.6)] scale-110' 
            : 'border-amber-600/50 shadow-lg'
        }`}>
          <img
            src="https://api.dicebear.com/9.x/notionists/svg?seed=Eden"
            alt="AI Barista"
            className="w-full h-full rounded-full bg-gradient-to-br from-amber-100 to-orange-100"
          />
          
          {/* Speaking indicator */}
          {isSpeaking && (
            <div className="absolute -bottom-2 -right-2 w-8 h-8 bg-gradient-to-r from-green-400 to-emerald-500 rounded-full border-4 border-black flex items-center justify-center animate-pulse">
              <div className="w-3 h-3 bg-white rounded-full animate-ping"></div>
            </div>
          )}
        </div>
        
        {/* Name tag */}
        <div className="mt-3 text-center">
          <div className="bg-gradient-to-r from-amber-900/90 to-orange-900/90 backdrop-blur-sm px-4 py-1.5 rounded-full border border-amber-600/50">
            <p className="text-amber-200 text-sm font-semibold">Eden</p>
            <p className="text-amber-400/70 text-xs">Your Barista</p>
          </div>
        </div>
      </div>
    </div>
  );
}
