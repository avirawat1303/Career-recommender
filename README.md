\# Career Path Recommendation System 🚀



An AI-powered career counseling platform that provides personalized career recommendations using machine learning.



\## 🌟 Features



\- \*\*Multi-user Authentication\*\* - Secure signup/login system

\- \*\*Smart Assessment Form\*\* - Searchable skill selection with 30+ skills organized by category

\- \*\*ML-Powered Recommendations\*\* - Top 5 career matches with confidence levels

\- \*\*Skill Gap Analysis\*\* - Shows skills you have and skills you need to learn

\- \*\*Career Details\*\* - Deep dive into each career with learning resources

\- \*\*History Tracking\*\* - View past assessments and track improvement over time



\## 🛠️ Tech Stack



\### Backend

\- \*\*Django 4.2\*\* - Web framework

\- \*\*Django REST Framework\*\* - API development

\- \*\*SQLite\*\* - Database

\- \*\*Scikit-learn\*\* - Machine learning

\- \*\*Pandas \& NumPy\*\* - Data processing



\### Frontend

\- \*\*React 18\*\* - UI framework

\- \*\*React Router\*\* - Navigation

\- \*\*Axios\*\* - HTTP client

\- \*\*Tailwind CSS\*\* - Styling



\## 📋 Prerequisites



\- Python 3.8+

\- Node.js 14+

\- pip

\- npm



\## 🚀 Installation \& Setup



\### Backend Setup



```bash

\# Navigate to backend folder

cd backend



\# Create virtual environment

python -m venv venv



\# Activate virtual environment

\# On Windows:

venv\\Scripts\\activate

\# On Mac/Linux:

source venv/bin/activate



\# Install dependencies

pip install -r requirements.txt



\# Run migrations

python manage.py migrate



\# Create superuser (for admin access)

python manage.py createsuperuser



\# Start development server

python manage.py runserver

```



Backend will run on: `http://127.0.0.1:8000/`



\### Frontend Setup



```bash

\# Navigate to frontend folder

cd frontend



\# Install dependencies

npm install



\# Start development server

npm start

```



Frontend will run on: `http://localhost:3000/`



\## 🎯 Usage



1\. \*\*Sign Up\*\* - Create a new account

2\. \*\*Take Assessment\*\* - Answer questions about your skills, interests, education, and work preferences

3\. \*\*View Recommendations\*\* - Get your top 5 career matches with detailed explanations

4\. \*\*Explore Careers\*\* - Click on any career to see detailed information and learning resources

5\. \*\*Track Progress\*\* - Retake assessments over time to see your improvement



\## 🤖 Machine Learning Model



The system uses a \*\*Decision Tree Classifier\*\* trained on synthetic data representing 30+ career paths and various skill combinations. The model:

\- Analyzes your skills, interests, education, and work style preferences

\- Calculates match probabilities for each career

\- Provides confidence levels (Very High, High, Moderate, Low)

\- Identifies skill gaps with specific learning recommendations



\## 🔐 API Endpoints



\### Authentication

\- `POST /api/auth/signup/` - Register new user

\- `POST /api/auth/login/` - Login user

\- `POST /api/auth/logout/` - Logout user



\### Assessments

\- `POST /api/assessment/` - Submit new assessment

\- `GET /api/assessment/history/` - Get user's assessment history

\- `GET /api/assessment/<id>/` - Get specific assessment details



\### Careers

\- `GET /api/careers/` - List all careers

\- `GET /api/careers/<name>/` - Get specific career details



\## 🌐 Admin Panel



Access the Django admin panel at `http://127.0.0.1:8000/admin/` to:

\- View all users and assessments

\- Manage career data

\- Monitor system usage





\## 📄 License



This project is open source and available under the \[MIT License](LICENSE).



\## 🙏 Acknowledgments



\- Built as a  project to understand full-stack development with ML integration

\- Special thanks to the Django, React, and Scikit-learn communities

