import React from 'react';
import StudentApp from './components/StudentApp';
import TeacherDashboard from './components/TeacherDashboard';

function App() {
  return (
    <div>
      <h1>Student Progress App</h1>
      <StudentApp />
      <hr />
      <TeacherDashboard />
    </div>
  );
}

export default App;
