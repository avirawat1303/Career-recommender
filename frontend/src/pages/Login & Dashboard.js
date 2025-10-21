
import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';

function LoginPage({ onLogin }) {
  const [formData, setFormData] = useState({ email: '', password: '' });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Mock login - replace with real API call
    const mockUser = { username: 'Demo User', email: formData.email, id: 1 };
    const mockToken = 'demo-token-' + Date.now();
    onLogin(mockUser, mockToken);
    navigate('/dashboard');
  };

  return (
    <div className="auth-page">
      <div className="auth-container">
        <h2>Welcome Back!</h2>
        <p className="auth-subtitle">Login to continue your career journey</p>
        {error && <div className="error-message">{error}</div>}
        <form onSubmit={handleSubmit} className="auth-form">
          <div className="form-group">
            <label>Email</label>
            <input
              type="email"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              required
              placeholder="your.email@example.com"
            />
          </div>
          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              value={formData.password}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              required
              placeholder="Enter your password"
            />
          </div>
          <button type="submit" className="btn btn-primary btn-full">Login</button>
        </form>
        <p className="auth-footer">
          Don't have an account? <Link to="/signup">Sign up here</Link>
        </p>
      </div>
    </div>
  );
}

function DashboardPage({ user }) {
  const mockHistory = [
    { id: 3, date: '2025-03-20', topCareer: 'Software Developer', score: 98 },
    { id: 2, date: '2025-02-05', topCareer: 'Software Developer', score: 92 },
    { id: 1, date: '2025-01-15', topCareer: 'Software Developer', score: 87 }
  ];

  return (
    <div className="dashboard-page">
      <div className="dashboard-container">
        <h1>Welcome back, {user?.username || 'User'}! 👋</h1>
        <div className="stats-grid">
          <div className="stat-card">
            <div className="stat-number">3</div>
            <div className="stat-label">Assessments Taken</div>
          </div>
          <div className="stat-card">
            <div className="stat-number">8</div>
            <div className="stat-label">Skills Tracked</div>
          </div>
          <div className="stat-card">
            <div className="stat-number">12</div>
            <div className="stat-label">Careers Explored</div>
          </div>
        </div>

        <div className="history-section">
          <h2>📅 Assessment History</h2>
          {mockHistory.map(assessment => (
            <div key={assessment.id} className="history-card">
              <div className="history-header">
                <h3>Assessment #{assessment.id}</h3>
                <span className="history-date">{assessment.date}</span>
              </div>
              <p className="history-result">
                Top Match: <strong>{assessment.topCareer}</strong> ({assessment.score}%)
              </p>
              <Link to="/recommendations" className="btn btn-small btn-secondary">
                View Results
              </Link>
            </div>
          ))}
        </div>

        <Link to="/assessment" className="btn btn-primary btn-large">
          Take New Assessment
        </Link>
      </div>
    </div>
  );
}

export { LoginPage, DashboardPage };