export interface AppConfig {
  pageTitle: string;
  pageDescription: string;
  companyName: string;

  supportsChatInput: boolean;
  supportsVideoInput: boolean;
  supportsScreenShare: boolean;
  isPreConnectBufferEnabled: boolean;

  logo: string;
  startButtonText: string;
  accent?: string;
  logoDark?: string;
  accentDark?: string;

  // for LiveKit Cloud Sandbox
  sandboxId?: string;
  agentName?: string;
}

export const APP_CONFIG_DEFAULTS: AppConfig = {
  companyName: 'Murf Coffee Shop',
  pageTitle: 'Murf Coffee Shop - AI Voice Barista',
  pageDescription: 'Order your favorite coffee with our AI voice barista',

  supportsChatInput: true,
  supportsVideoInput: true,
  supportsScreenShare: true,
  isPreConnectBufferEnabled: true,

  logo: '/lk-logo.svg',
  accent: '#7c3aed',
  logoDark: '/lk-logo-dark.svg',
  accentDark: '#a78bfa',
  startButtonText: 'Start Ordering',

  // for LiveKit Cloud Sandbox
  sandboxId: undefined,
  agentName: undefined,
};
