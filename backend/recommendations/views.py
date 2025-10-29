"""
Recommendations API Views

API endpoints for:
- Submitting assessments
- Viewing recommendations
- Getting assessment history
- Career details
"""

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Assessment, Recommendation, CareerDetail
from .serializers import (
    AssessmentSubmissionSerializer,
    AssessmentSerializer,
    AssessmentListSerializer,
    RecommendationSerializer,
    CareerDetailSerializer
)
from .services import create_assessment_with_recommendations, get_user_assessment_history


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_assessment(request):
    """
    Submit Career Assessment
    
    Method: POST
    URL: /api/assessment/
    
    Request Body (JSON):
    {
        "skills": ["Programming", "Data Analysis", "Design"],
        "interests": ["Technology & Innovation", "Arts & Design"],
        "education": "Bachelor's Degree",
        "work_style": "Remote / Work from home"
    }
    
    Response (Success - 201):
    {
        "assessment_id": 1,
        "message": "Assessment submitted successfully",
        "recommendations": [
            {
                "rank": 1,
                "career_name": "Software Developer",
                "match_score": 92.0,
                "confidence_level": "Very High",
                "matching_skills": [...],
                "missing_skills": [...],
                "completeness_percent": 60.0,
                ...
            },
            ...
        ]
    }
    
    Response (Error - 400):
    {
        "skills": ["Please select at least 3 skills"],
        "interests": ["Please select at least 2 interests"]
    }
    """
    
    # Validate input data
    serializer = AssessmentSubmissionSerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Get validated data
    assessment_data = serializer.validated_data
    
    try:
        # Create assessment and get recommendations
        result = create_assessment_with_recommendations(
            user=request.user,
            assessment_data=assessment_data
        )
        
        assessment = result['assessment']
        recommendations = result['recommendations']
        
        # Serialize recommendations for response
        recommendations_data = RecommendationSerializer(
            recommendations,
            many=True
        ).data
        
        # Check if ML model failed
        if 'error' in result:
            return Response({
                'assessment_id': assessment.id,
                'message': 'Assessment submitted but ML prediction failed',
                'error': result['error'],
                'recommendations': recommendations_data
            }, status=status.HTTP_201_CREATED)
        
        # Success response
        return Response({
            'assessment_id': assessment.id,
            'message': 'Assessment submitted successfully',
            'recommendations': recommendations_data
        }, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        # Unexpected error
        return Response({
            'error': 'Failed to process assessment',
            'detail': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def assessment_history(request):
    """
    Get User's Assessment History
    
    Method: GET
    URL: /api/assessment/history/
    
    Response (200):
    [
        {
            "id": 3,
            "skills": [...],
            "interests": [...],
            "education_level": "Bachelor's Degree",
            "work_style": "Remote",
            "created_at": "2025-03-20T10:30:00Z",
            "top_recommendation": {
                "career_name": "Software Developer",
                "match_score": 98.0
            },
            "recommendations_count": 5
        },
        {
            "id": 2,
            ...
        }
    ]
    """
    
    # Get all assessments for current user
    assessments = get_user_assessment_history(request.user)
    
    # Serialize with lightweight serializer
    serializer = AssessmentListSerializer(assessments, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def assessment_detail(request, assessment_id):
    """
    Get Detailed Assessment with All Recommendations
    
    Method: GET
    URL: /api/assessment/<id>/
    
    Response (200):
    {
        "id": 1,
        "username": "john",
        "skills": [...],
        "interests": [...],
        "education_level": "Bachelor's Degree",
        "work_style": "Remote",
        "created_at": "2025-03-20T10:30:00Z",
        "recommendations": [
            {
                "rank": 1,
                "career_name": "Software Developer",
                "match_score": 92.0,
                "confidence_level": "Very High",
                "matching_skills": [...],
                "missing_skills": [...],
                "completeness_percent": 60.0,
                "rationale": {...}
            },
            ...
        ]
    }
    
    Response (404):
    {
        "error": "Assessment not found"
    }
    
    Response (403):
    {
        "error": "You don't have permission to view this assessment"
    }
    """
    
    # Get assessment or return 404
    assessment = get_object_or_404(Assessment, id=assessment_id)
    
    # Check if user owns this assessment
    if assessment.user != request.user:
        return Response({
            'error': 'You don\'t have permission to view this assessment'
        }, status=status.HTTP_403_FORBIDDEN)
    
    # Serialize with full data (includes recommendations)
    serializer = AssessmentSerializer(assessment)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def career_list(request):
    """
    Get List of All Careers
    
    Method: GET
    URL: /api/careers/
    
    Response (200):
    [
        {
            "id": 1,
            "career_name": "Software Developer",
            "description": "...",
            "job_growth": "+22%",
            ...
        },
        ...
    ]
    """
    
    careers = CareerDetail.objects.all()
    serializer = CareerDetailSerializer(careers, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def career_detail(request, career_name):
    """
    Get Detailed Information About a Career
    
    Method: GET
    URL: /api/careers/<career_name>/
    
    Example: /api/careers/Software Developer/
    
    Response (200):
    {
        "id": 1,
        "career_name": "Software Developer",
        "description": "Design, develop, and maintain software...",
        "requirements": {
            "education": "Bachelor's Degree",
            "skills": ["Programming", "Problem Solving", ...],
            "certifications": ["AWS", ...]
        },
        "salary_info": {
            "entry": "$60,000 - $80,000",
            "mid": "$80,000 - $120,000",
            "senior": "$120,000 - $180,000+"
        },
        "job_growth": "+22% (Much faster than average)",
        "work_environment": "...",
        "learning_resources": [...],
        "related_careers": [...]
    }
    
    Response (404):
    {
        "error": "Career not found"
    }
    """
    
    # Get career or return 404
    career = get_object_or_404(CareerDetail, career_name=career_name)
    
    serializer = CareerDetailSerializer(career)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


"""
🔑 KEY LEARNING POINTS:

1. PERMISSION CLASSES:
   - @permission_classes([IsAuthenticated])
   - User MUST be logged in to access
   - request.user automatically set by Django

2. REQUEST OBJECT:
   - request.data: JSON body sent by client
   - request.user: Currently logged-in user
   - request.method: HTTP method (GET, POST, etc.)

3. RESPONSE OBJECT:
   - Response(data, status=...): Return JSON
   - status codes from rest_framework.status
   - Automatically serializes to JSON

4. ERROR HANDLING:
   - try/except for unexpected errors
   - get_object_or_404: Returns 404 if not found
   - Check permissions before processing

5. SERIALIZER VALIDATION:
   - serializer.is_valid(): Run validation
   - serializer.errors: Dictionary of errors
   - serializer.validated_data: Clean data

6. PERMISSION CHECKING:
   - Check if user owns resource
   - Return 403 FORBIDDEN if not
   - Important for security!

7. URL PARAMETERS:
   - assessment_id from URL: /api/assessment/<assessment_id>/
   - career_name from URL: /api/careers/<career_name>/
   - Captured in function parameters

REQUEST/RESPONSE FLOW:
1. Client sends HTTP request
2. Django routes to view function
3. View validates authentication
4. View validates input data
5. View processes (database, ML, etc.)
6. View returns HTTP response with JSON

SECURITY FEATURES:
✓ Authentication required
✓ Permission checking (user owns data)
✓ Input validation
✓ Error handling (no data leaks)
✓ CSRF protection (automatic)
"""