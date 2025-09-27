import React from 'react';
import StudentApp from './StudentApp';
import TeacherDashboard from './TeacherDashboard';

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
