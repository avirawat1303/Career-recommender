import React from 'react';
import { Link } from 'react-router-dom';
import './RecommendationsPage.css';

function RecommendationsPage() {
  // Example static data; can later be replaced with ML API results
  const recommendations = [
    {
      career: 'Data Scientist',
      description: 'Analyze and interpret complex data to help organizations make better decisions.',
      skills: ['Python', 'Statistics', 'Machine Learning']
    },
    {
      career: 'UX Designer',
      description: 'Design user-friendly digital interfaces that enhance customer experiences.',
      skills: ['Design Thinking', 'Figma', 'User Research']
    },
    {
      career: 'Software Engineer',
      description: 'Develop, test, and maintain software systems and applications.',
      skills: ['C++', 'Algorithms', 'System Design']
    }
  ];

  return (
    <div className="recommendations-page">
      <div className="recommendations-container">
        <h1>Your Career Recommendations</h1>
        <p>Based on your assessment, here are your top matches:</p>

        <div className="recommendations-list">
          {recommendations.map((rec, index) => (
            <div key={index} className="recommendation-card">
              <h2>{rec.career}</h2>
              <p>{rec.description}</p>
              <strong>Key Skills:</strong>
              <ul>
                {rec.skills.map((skill, i) => (
                  <li key={i}>✅ {skill}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="cta-section">
          <Link to="/assessment" className="btn btn-secondary">Retake Assessment</Link>
          <Link to="/learning" className="btn btn-primary">View Learning Resources</Link>
        </div>
      </div>
    </div>
  );
}

export default RecommendationsPage;
