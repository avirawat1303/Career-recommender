import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './AssessmentPage.css';

function AssessmentPage() {
  const navigate = useNavigate();
  const [answers, setAnswers] = useState({
    skills: '',
    interests: '',
    workStyle: '',
    education: ''
  });

  const handleChange = (e) => {
    setAnswers({ ...answers, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Assessment Answers:', answers);
    navigate('/recommendations');
  };

  return (
    <div className="assessment-page">
      <div className="assessment-container">
        <h1>Career Assessment</h1>
        <p>Answer a few questions to help our AI understand your preferences.</p>

        <form onSubmit={handleSubmit} className="assessment-form">
          <label>What are your top 3 skills?</label>
          <input 
            type="text"
            name="skills"
            placeholder="e.g., Problem Solving, Design, Communication"
            value={answers.skills}
            onChange={handleChange}
            required
          />

          <label>What are your main interests?</label>
          <input 
            type="text"
            name="interests"
            placeholder="e.g., Technology, Art, Finance"
            value={answers.interests}
            onChange={handleChange}
            required
          />

          <label>Preferred work style?</label>
          <select name="workStyle" value={answers.workStyle} onChange={handleChange} required>
            <option value="">Select...</option>
            <option value="Team-oriented">Team-oriented</option>
            <option value="Independent">Independent</option>
            <option value="Flexible">Flexible</option>
          </select>

          <label>Highest education level?</label>
          <select name="education" value={answers.education} onChange={handleChange} required>
            <option value="">Select...</option>
            <option value="High School">High School</option>
            <option value="Undergraduate">Undergraduate</option>
            <option value="Postgraduate">Postgraduate</option>
          </select>

          <button type="submit" className="btn btn-primary">Get Recommendations</button>
        </form>
      </div>
    </div>
  );
}

export default AssessmentPage;
