
import sys
import os
from django.conf import settings

# Add ml_model to Python path
ml_model_path = os.path.join(settings.BASE_DIR, 'ml_model')
if ml_model_path not in sys.path:
    sys.path.insert(0, ml_model_path)

# Try importing ML prediction function
ML_MODEL_AVAILABLE = False
predict_careers = None

try:
    # Try importing from ml_model package
    from ml_model.predict import predict_careers
    ML_MODEL_AVAILABLE = True
    print("✓ ML model loaded successfully")
except ImportError as e:
    print(f"⚠️  ML model not available: {e}")
    print("   Using mock recommendations instead")
    ML_MODEL_AVAILABLE = False

from .models import Assessment, Recommendation

def create_assessment_with_recommendations(user, assessment_data):
    
    # Step 1: Create and save assessment
    assessment = Assessment.objects.create(
        user=user,
        skills=assessment_data['skills'],
        interests=assessment_data['interests'],
        education_level=assessment_data['education'],
        work_style=assessment_data['work_style']
    )
    
    # Step 2: Get ML predictions
    if ML_MODEL_AVAILABLE:
        try:
            # Call ML model
            ml_predictions = predict_careers(assessment_data)
            
            # Step 3: Save each recommendation
            recommendations = []
            for pred in ml_predictions:
                recommendation = Recommendation.objects.create(
                    assessment=assessment,
                    career_name=pred['career_name'],
                    match_score=pred['match_score'],
                    confidence_level=pred['confidence_level'],
                    rank=pred['rank'],
                    matching_skills=pred['matching_skills'],
                    missing_skills=pred['missing_skills'],
                    completeness_percent=pred['completeness_percent'],
                    rationale={
                        'interests_alignment': assessment_data['interests'],
                        'education_match': True,  # Can add logic here
                        'work_style_match': True
                    }
                )
                recommendations.append(recommendation)
            
            return {
                'assessment': assessment,
                'recommendations': recommendations
            }
        
        except Exception as e:
            # ML model failed - log error but don't crash
            print(f"❌ ML prediction error: {e}")
            # Return assessment with empty recommendations
            return {
                'assessment': assessment,
                'recommendations': [],
                'error': str(e)
            }
    
    else:
        # ML model not available - return mock data for testing
        print("⚠️  Using mock recommendations (ML model not available)")
        recommendations = create_mock_recommendations(assessment, assessment_data)
        return {
            'assessment': assessment,
            'recommendations': recommendations
        }


def create_mock_recommendations(assessment, assessment_data):
    mock_careers = [
        {
            'career_name': 'Software Developer',
            'match_score': 92.0,
            'confidence_level': 'Very High',
            'rank': 1,
            'matching_skills': assessment_data['skills'][:3] if len(assessment_data['skills']) >= 3 else assessment_data['skills'],
            'missing_skills': ['Git', 'SQL'],
            'completeness_percent': 60.0
        },
        {
            'career_name': 'Data Scientist',
            'match_score': 85.0,
            'confidence_level': 'High',
            'rank': 2,
            'matching_skills': assessment_data['skills'][:2] if len(assessment_data['skills']) >= 2 else assessment_data['skills'],
            'missing_skills': ['Machine Learning', 'Statistics'],
            'completeness_percent': 40.0
        },
        {
            'career_name': 'UX/UI Designer',
            'match_score': 78.0,
            'confidence_level': 'High',
            'rank': 3,
            'matching_skills': assessment_data['skills'][:2] if len(assessment_data['skills']) >= 2 else assessment_data['skills'],
            'missing_skills': ['Figma', 'User Research'],
            'completeness_percent': 50.0
        },
        {
            'career_name': 'Web Developer',
            'match_score': 72.0,
            'confidence_level': 'Moderate',
            'rank': 4,
            'matching_skills': assessment_data['skills'][:1] if len(assessment_data['skills']) >= 1 else [],
            'missing_skills': ['JavaScript', 'React'],
            'completeness_percent': 45.0
        },
        {
            'career_name': 'Product Manager',
            'match_score': 68.0,
            'confidence_level': 'Moderate',
            'rank': 5,
            'matching_skills': assessment_data['skills'][:1] if len(assessment_data['skills']) >= 1 else [],
            'missing_skills': ['Product Strategy', 'Agile'],
            'completeness_percent': 50.0
        }
    ]
    
    # Create recommendation objects
    recommendations = []
    for career_data in mock_careers:
        recommendation = Recommendation.objects.create(
            assessment=assessment,
            **career_data,
            rationale={
                'interests_alignment': assessment_data['interests'],
                'education_match': True,
                'work_style_match': True,
                'note': 'Mock data - ML model not available'
            }
        )
        recommendations.append(recommendation)
    
    return recommendations


def get_user_assessment_history(user):
    assessments = Assessment.objects.filter(
        user=user
    ).prefetch_related('recommendations').order_by('-created_at')
    
    return assessments
