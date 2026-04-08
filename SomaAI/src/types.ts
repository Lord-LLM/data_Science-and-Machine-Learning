export interface UserProfile {
  uid: string;
  displayName: string;
  email: string;
  preferredLanguage: 'English' | 'Swahili' | 'Sheng';
  gradeLevel: string;
  createdAt: string;
}

export interface StudySession {
  id?: string;
  uid: string;
  concept: string;
  explanation: string;
  analogy: string;
  imageUrl?: string;
  timestamp: string;
}

export type AppStep = 'welcome' | 'tutor' | 'history' | 'profile';
