import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';

function HomePage() {
  return (
    <div className="home-page">
      <div className="hero-section">
        <h1 className="hero-title">Discover Your Ideal Career Path with AI</h1>
        <p className="hero-subtitle">
          Get personalized career recommendations powered by machine learning
        </p>
        <div className="hero-buttons">
          <Link to="/signup" className="btn btn-primary">Get Started</Link>
          <Link to="/login" className="btn btn-secondary">Login</Link>
        </div>
      </div>

      <div className="features-section">
        <h2>How It Works</h2>
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">📝</div>
            <h3>Take Assessment</h3>
            <p>Answer questions about your skills, interests, education, and work preferences</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🤖</div>
            <h3>AI Analysis</h3>
            <p>Our machine learning model analyzes your profile to find the best career matches</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🎯</div>
            <h3>Get Recommendations</h3>
            <p>Receive top 5 career suggestions with detailed explanations and skill gaps</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">📚</div>
            <h3>Learn & Grow</h3>
            <p>Access learning resources and track your progress over time</p>
          </div>
        </div>
      </div>

      <div className="value-props">
        <h2>Why Choose Career Path Recommender?</h2>
        <ul className="benefits-list">
          <li>✅ Personalized recommendations based on YOUR unique profile</li>
          <li>✅ ML-powered insights with confidence scoring</li>
          <li>✅ Detailed skill gap analysis with learning resources</li>
          <li>✅ Track your career journey over time</li>
          <li>✅ 30+ careers across multiple industries</li>
        </ul>
      </div>

      <div className="cta-section">
        <h2>Ready to Find Your Perfect Career?</h2>
        <Link to="/signup" className="btn btn-large btn-primary">Start Your Journey</Link>
      </div>
    </div>
  );
}

export default HomePage;