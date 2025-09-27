import React, { useState, useEffect } from "react";
import axios from "axios";

const BASE_URL = process.env.REACT_APP_BACKEND_URL;

function TeacherPage() {
  const [data, setData] = useState([]);
  const [studentId, setStudentId] = useState(1);
  const [unitId, setUnitId] = useState(1);

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    try {
      const res = await axios.get(`${BASE_URL}/teacher_dashboard`);
      setData(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const generateHomework = async () => {
    try {
      const res = await axios.post(`${BASE_URL}/generate_homework`, {
        student_id: studentId,
        unit_id: unitId,
        num_questions: 5
      }, { responseType: 'blob' });

      const url = window.URL.createObjectURL(new Blob([res.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `homework_student_${studentId}_unit_${unitId}.csv`);
      document.body.appendChild(link);
      link.click();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Teacher Dashboard</h2>
      <table border="1">
        <thead>
          <tr>
            <th>Student</th><th>Unit</th><th>Topic</th><th>Levels</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              <td>{row.student_id}</td>
              <td>{row.unit_id}</td>
              <td>{row.topic}</td>
              <td>{row.understanding_level.join(", ")}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <h3>Generate Homework</h3>
      <input type="number" value={studentId} onChange={e=>setStudentId(parseInt(e.target.value))} placeholder="Student ID"/>
      <input type="number" value={unitId} onChange={e=>setUnitId(parseInt(e.target.value))} placeholder="Unit ID"/>
      <button onClick={generateHomework}>Generate Homework</button>
    </div>
  );
}

export default TeacherPage;
