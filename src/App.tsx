/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { 
  BookOpen, 
  Camera, 
  History, 
  User, 
  Send, 
  Zap, 
  Loader2, 
  ChevronRight, 
  ArrowLeft,
  Sparkles,
  LogOut,
  Globe,
  Trash2
} from 'lucide-react';
import { useAuthState } from 'react-firebase-hooks/auth';
import { signInWithPopup, GoogleAuthProvider, signOut } from 'firebase/auth';
import { 
  collection, 
  addDoc, 
  query, 
  where, 
  orderBy, 
  onSnapshot, 
  doc, 
  setDoc, 
  getDoc,
  deleteDoc,
  Timestamp 
} from 'firebase/firestore';
import { auth, db } from './firebase';
import { cn } from './lib/utils';
import { AppStep, UserProfile, StudySession } from './types';
import * as gemini from './services/geminiService';

export default function App() {
  const [user, loadingAuth] = useAuthState(auth);
  const [step, setStep] = useState<AppStep>('welcome');
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [sessions, setSessions] = useState<StudySession[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [currentSession, setCurrentSession] = useState<StudySession | null>(null);
  const [image, setImage] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Sync Profile
  useEffect(() => {
    if (user) {
      const docRef = doc(db, 'users', user.uid);
      const unsubscribe = onSnapshot(docRef, (docSnap) => {
        if (docSnap.exists()) {
          setProfile(docSnap.data() as UserProfile);
        } else {
          const newProfile: UserProfile = {
            uid: user.uid,
            displayName: user.displayName || 'Student',
            email: user.email || '',
            preferredLanguage: 'Swahili',
            gradeLevel: 'Secondary',
            createdAt: new Date().toISOString()
          };
          setDoc(docRef, newProfile);
        }
      });
      return () => unsubscribe();
    } else {
      setProfile(null);
    }
  }, [user]);

  // Sync Sessions
  useEffect(() => {
    if (user) {
      const q = query(
        collection(db, 'sessions'),
        where('uid', '==', user.uid),
        orderBy('timestamp', 'desc')
      );
      const unsubscribe = onSnapshot(q, (snapshot) => {
        setSessions(snapshot.docs.map(doc => ({ id: doc.id, ...doc.data() } as StudySession)));
      });
      return () => unsubscribe();
    }
  }, [user]);

  const handleLogin = async () => {
    const provider = new GoogleAuthProvider();
    try {
      await signInWithPopup(auth, provider);
    } catch (error) {
      console.error("Login failed", error);
    }
  };

  const handleExplain = async () => {
    if (!input.trim() && !image) return;
    setLoading(true);
    setError(null);
    try {
      const result = await gemini.explainConcept(
        input || "Explain the content in this image", 
        profile?.preferredLanguage || 'Swahili',
        image || undefined
      );
      
      const session: StudySession = {
        uid: user!.uid,
        concept: input || "Visual Analysis",
        explanation: result.explanation,
        analogy: result.analogy,
        imageUrl: image || undefined,
        timestamp: new Date().toISOString()
      };

      await addDoc(collection(db, 'sessions'), session);
      setCurrentSession(session);
      setInput('');
      setImage(null);
    } catch (err) {
      console.error(err);
      setError("Samahani! Something went wrong while thinking. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setImage(reader.result as string);
      };
      reader.readAsDataURL(file);
    }
  };

  const deleteSession = async (id: string) => {
    await deleteDoc(doc(db, 'sessions', id));
  };

  if (loadingAuth) {
    return (
      <div className="min-h-screen bg-background flex items-center justify-center">
        <Loader2 className="animate-spin text-violet" size={48} />
      </div>
    );
  }

  return (
    <div className="min-h-screen flex flex-col">
      {/* Header */}
      <header className="p-6 flex justify-between items-center z-50 glass sticky top-0">
        <div className="flex items-center gap-2 cursor-pointer" onClick={() => setStep('welcome')}>
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-violet to-magenta flex items-center justify-center neon-border">
            <BookOpen className="text-white w-6 h-6" />
          </div>
          <h1 className="text-2xl font-display font-bold tracking-tight neon-text">SomaAI</h1>
        </div>
        
        {user ? (
          <div className="flex items-center gap-4">
            <button onClick={() => setStep('history')} className="p-2 hover:bg-white/5 rounded-full transition-colors">
              <History size={20} />
            </button>
            <button onClick={() => setStep('profile')} className="p-2 hover:bg-white/5 rounded-full transition-colors">
              <User size={20} />
            </button>
            <button onClick={() => signOut(auth)} className="p-2 hover:bg-white/5 rounded-full transition-colors text-red-400">
              <LogOut size={20} />
            </button>
          </div>
        ) : (
          <button 
            onClick={handleLogin}
            className="px-6 py-2 rounded-full bg-violet text-white font-medium hover:bg-magenta transition-all"
          >
            Login
          </button>
        )}
      </header>

      <main className="flex-1 max-w-4xl mx-auto w-full p-6 pb-24">
        <AnimatePresence mode="wait">
          {!user && (
            <motion.div 
              key="login"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="flex flex-col items-center justify-center min-h-[70vh] text-center gap-8"
            >
              <div className="relative">
                <div className="absolute -inset-4 bg-violet/20 blur-3xl rounded-full animate-pulse-glow" />
                <h2 className="text-5xl md:text-6xl font-display font-black leading-tight">
                  Your Personal <br />
                  <span className="text-transparent bg-clip-text bg-gradient-to-r from-violet to-magenta">STEM Tutor</span>
                </h2>
              </div>
              <p className="text-xl text-text-soft/60 max-w-xl">
                Master complex concepts with localized analogies and code-switching. Snap a photo or type a question to start learning.
              </p>
              <button 
                onClick={handleLogin}
                className="px-10 py-4 rounded-2xl bg-gradient-to-r from-violet to-magenta text-white font-bold text-lg hover:scale-105 transition-transform flex items-center gap-3"
              >
                Get Started for Free
                <ArrowLeft className="rotate-180" />
              </button>
            </motion.div>
          )}

          {user && step === 'welcome' && (
            <motion.div 
              key="tutor-home"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="space-y-8"
            >
              <div className="flex items-center justify-between">
                <div>
                  <h2 className="text-3xl font-display font-bold">Habari, {profile?.displayName}!</h2>
                  <p className="text-text-soft/60">What are we learning today?</p>
                </div>
                <div className="flex items-center gap-2 px-4 py-2 glass rounded-full text-xs font-medium text-violet">
                  <Globe size={14} />
                  {profile?.preferredLanguage} Mode
                </div>
              </div>

              <div className="glass p-8 rounded-3xl space-y-6">
                <div className="relative">
                  <textarea 
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Ask me anything... (e.g., 'How does photosynthesis work?')"
                    className="w-full bg-white/5 border border-white/10 rounded-2xl p-6 min-h-[150px] text-lg focus:outline-none focus:ring-2 focus:ring-violet/50 transition-all resize-none"
                  />
                  <div className="absolute bottom-4 right-4 flex gap-2">
                    <button 
                      onClick={() => fileInputRef.current?.click()}
                      className="w-12 h-12 rounded-xl glass flex items-center justify-center text-text-soft/60 hover:text-violet transition-colors"
                    >
                      <Camera size={20} />
                    </button>
                    <input 
                      type="file" 
                      ref={fileInputRef} 
                      onChange={handleImageUpload} 
                      accept="image/*" 
                      className="hidden" 
                    />
                    <button 
                      onClick={handleExplain}
                      disabled={loading || (!input.trim() && !image)}
                      className="w-12 h-12 rounded-xl bg-violet text-white flex items-center justify-center hover:bg-magenta transition-all disabled:opacity-50"
                    >
                      {loading ? <Loader2 className="animate-spin" /> : <Send size={20} />}
                    </button>
                  </div>
                </div>

                {image && (
                  <div className="relative w-32 h-32 rounded-xl overflow-hidden border border-white/10">
                    <img src={image} alt="Upload" className="w-full h-full object-cover" />
                    <button 
                      onClick={() => setImage(null)}
                      className="absolute top-1 right-1 bg-black/50 text-white p-1 rounded-full hover:bg-red-500 transition-colors"
                    >
                      <Trash2 size={12} />
                    </button>
                  </div>
                )}

                {error && (
                  <motion.div 
                    initial={{ opacity: 0, y: -10 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="p-4 rounded-xl bg-red-500/10 border border-red-500/20 text-red-400 text-sm flex items-center gap-3"
                  >
                    <Zap size={16} className="shrink-0" />
                    {error}
                  </motion.div>
                )}
              </div>

              {currentSession && (
                <motion.div 
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  className="space-y-6"
                >
                  <div className="glass p-8 rounded-3xl border-l-4 border-violet space-y-4">
                    <div className="flex items-center gap-2 text-violet">
                      <Sparkles size={18} />
                      <h3 className="font-bold uppercase tracking-widest text-xs">Explanation</h3>
                    </div>
                    <p className="text-lg leading-relaxed">{currentSession.explanation}</p>
                  </div>

                  <div className="glass p-8 rounded-3xl border-l-4 border-magenta space-y-4">
                    <div className="flex items-center gap-2 text-magenta">
                      <Zap size={18} />
                      <h3 className="font-bold uppercase tracking-widest text-xs">Local Analogy</h3>
                    </div>
                    <p className="text-lg leading-relaxed italic text-text-soft/80">"{currentSession.analogy}"</p>
                  </div>
                </motion.div>
              )}
            </motion.div>
          )}

          {user && step === 'history' && (
            <motion.div 
              key="history"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="space-y-6"
            >
              <div className="flex items-center gap-4 mb-8">
                <button onClick={() => setStep('welcome')} className="p-2 hover:bg-white/5 rounded-full">
                  <ArrowLeft size={20} />
                </button>
                <h2 className="text-3xl font-display font-bold">Study History</h2>
              </div>

              <div className="grid grid-cols-1 gap-4">
                {sessions.length === 0 ? (
                  <div className="text-center py-20 text-text-soft/40">
                    No sessions yet. Start learning!
                  </div>
                ) : (
                  sessions.map((s) => (
                    <div 
                      key={s.id} 
                      className="glass p-6 rounded-2xl flex justify-between items-center group cursor-pointer hover:bg-white/10 transition-all"
                      onClick={() => {
                        setCurrentSession(s);
                        setStep('welcome');
                      }}
                    >
                      <div className="flex items-center gap-4">
                        <div className="w-12 h-12 rounded-xl bg-violet/10 flex items-center justify-center text-violet">
                          <BookOpen size={20} />
                        </div>
                        <div>
                          <h4 className="font-bold">{s.concept}</h4>
                          <p className="text-xs text-text-soft/40">{new Date(s.timestamp).toLocaleDateString()}</p>
                        </div>
                      </div>
                      <div className="flex items-center gap-4">
                        <ChevronRight className="text-text-soft/20 group-hover:text-violet transition-colors" />
                        <button 
                          onClick={(e) => {
                            e.stopPropagation();
                            deleteSession(s.id!);
                          }}
                          className="p-2 text-red-400/40 hover:text-red-400 transition-colors"
                        >
                          <Trash2 size={16} />
                        </button>
                      </div>
                    </div>
                  ))
                )}
              </div>
            </motion.div>
          )}

          {user && step === 'profile' && profile && (
            <motion.div 
              key="profile"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="space-y-8"
            >
              <div className="flex items-center gap-4 mb-8">
                <button onClick={() => setStep('welcome')} className="p-2 hover:bg-white/5 rounded-full">
                  <ArrowLeft size={20} />
                </button>
                <h2 className="text-3xl font-display font-bold">Profile Settings</h2>
              </div>

              <div className="glass p-8 rounded-3xl space-y-8">
                <div className="space-y-2">
                  <label className="text-xs font-bold text-text-soft/40 uppercase">Preferred Language Mode</label>
                  <div className="flex gap-4">
                    {['English', 'Swahili', 'Sheng'].map((lang) => (
                      <button
                        key={lang}
                        onClick={() => setDoc(doc(db, 'users', user.uid), { ...profile, preferredLanguage: lang })}
                        className={cn(
                          "flex-1 py-3 rounded-xl border transition-all",
                          profile.preferredLanguage === lang 
                            ? "bg-violet/20 border-violet text-violet font-bold" 
                            : "bg-white/5 border-white/10 text-text-soft/60 hover:bg-white/10"
                        )}
                      >
                        {lang}
                      </button>
                    ))}
                  </div>
                </div>

                <div className="space-y-2">
                  <label className="text-xs font-bold text-text-soft/40 uppercase">Grade Level</label>
                  <select 
                    value={profile.gradeLevel}
                    onChange={(e) => setDoc(doc(db, 'users', user.uid), { ...profile, gradeLevel: e.target.value })}
                    className="w-full bg-white/5 border border-white/10 rounded-xl p-4 focus:outline-none focus:ring-2 focus:ring-violet/50"
                  >
                    <option value="Primary">Primary School</option>
                    <option value="Secondary">Secondary School</option>
                    <option value="University">University / College</option>
                  </select>
                </div>

                <div className="pt-6 border-t border-white/5 flex items-center gap-4">
                  <div className="w-16 h-16 rounded-full bg-gradient-to-br from-violet to-magenta p-0.5">
                    <img src={user.photoURL || ''} alt="Avatar" className="w-full h-full rounded-full object-cover" />
                  </div>
                  <div>
                    <h4 className="font-bold text-xl">{profile.displayName}</h4>
                    <p className="text-text-soft/40 text-sm">{profile.email}</p>
                  </div>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </main>

      {/* Loading Overlay */}
      {loading && (
        <div className="fixed inset-0 bg-background/80 backdrop-blur-sm z-[100] flex flex-col items-center justify-center gap-6">
          <div className="relative">
            <div className="w-24 h-24 rounded-full border-4 border-violet/20 border-t-violet animate-spin" />
            <Zap className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-violet animate-pulse" size={32} />
          </div>
          <div className="text-center space-y-2">
            <h3 className="text-xl font-display font-bold neon-text">SomaAI is Thinking...</h3>
            <p className="text-text-soft/40 text-sm animate-pulse">Creating your localized analogy</p>
          </div>
        </div>
      )}
    </div>
  );
}
