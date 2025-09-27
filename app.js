import React from 'react';
import './index.css';
import LoginCard from './components/LoginCard';

function App() {
  return (
    <div className="container">
      <LoginCard title="Student Login" placeholder1="Student ID" placeholder2="Password" footer="Need help? Contact your advisor." />
      <LoginCard title="Teacher Login" placeholder1="Email" placeholder2="Password" footer="Forgot password? Reset here." />
    </div>
  );
}

export default App;
