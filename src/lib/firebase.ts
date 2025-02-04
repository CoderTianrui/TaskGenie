import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';
import { getFirestore } from 'firebase/firestore';

// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBPkojtWkj1_r-Lk-LvzPduoqzOaUDLFik",
  authDomain: "task-management-21af5.firebaseapp.com",
  projectId: "task-management-21af5",
  storageBucket: "task-management-21af5.appspot.com",
  messagingSenderId: "664579727363",
  appId: "1:664579727363:web:9a297c3247951af8e3ee36",
  measurementId: "G-FPRSJYC50X"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase services
export const auth = getAuth(app);
export const db = getFirestore(app);

// Set Firebase Auth language
auth.languageCode = 'en'; // Changed to English