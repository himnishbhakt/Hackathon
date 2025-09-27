import React, { useState, useEffect } from "react";
import axios from "axios";

const BASE_URL = process.env.REACT_APP_BACKEND_URL;

function StudentPage({ studentId, className, subject }) {
  const [unitId, setUnitId] = useState(1);
  const [topics, setTopics] = useState([]);

  useEffect(() => {
    fetchTopics(unitId);
  }, [unitId]);

  const fetchTopics = async (unit) => {
    try {
      const res = await axios.get(`${BASE_URL}/get_topics?unit_id=${unit}`);
      setTopics(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const sendResponse = async (topic, level) => {
    try {
      await axios.post(`${BASE_URL}/log_response`, {
        student_id: studentId,
        class: className,
        subject: subject,
        unit_id: unitId,
        topic: topic,
        understanding_level: level
      });
      alert(`Submitted ${level} for ${topic}`);
    } catch (err) {
      console.error(err);
      alert("Failed to submit response");
    }
  };

  return (
    <div>
      <h2>Select Unit</h2>
      <input type="number" value={unitId} onChange={e=>setUnitId(parseInt(e.target.value))} />
      <h2>Topics for Unit {unitId}</h2>
      {topics.map(topic => (
        <div key={topic}>
          <h3>{topic}</h3>
          <button onClick={()=>sendResponse(topic,"green")}>Green</button>
          <button onClick={()=>sendResponse(topic,"yellow")}>Yellow</button>
          <button onClick={()=>sendResponse(topic,"red")}>Red</button>
        </div>
      ))}
    </div>
  );
}

export default StudentPage;
