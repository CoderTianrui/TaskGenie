import React from 'react';
import { Auth } from './components/Auth';
import { TaskList } from './components/TaskList';
import { AddTask } from './components/AddTask';
import { auth } from './lib/firebase';
import { useAuthState } from 'react-firebase-hooks/auth';

function App() {
  const [user] = useAuthState(auth);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-4xl font-bold text-indigo-900 tracking-tight">
            Family Task Manager
          </h1>
          <Auth />
        </div>
        
        {user && (
          <div className="space-y-8">
            <div className="bg-white rounded-xl shadow-lg p-8 border border-indigo-100">
              <h2 className="text-2xl font-semibold text-indigo-900 mb-6">Add New Task</h2>
              <AddTask />
            </div>
            <TaskList />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;