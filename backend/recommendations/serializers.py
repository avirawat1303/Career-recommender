from rest_framework import serializers
from .models import Assessment, Recommendation, CareerDetail

class AssessmentSubmissionSerializer(serializers.Serializer):
    
    skills = serializers.ListField(
        child=serializers.CharField(max_length=100),
        min_length=3,
        help_text="List of skills (minimum 3)"
    )
    
    interests = serializers.ListField(
        child=serializers.CharField(max_length=100),
        min_length=2,
        help_text="List of interests (minimum 2)"
    )
    
    education = serializers.CharField(
        max_length=100,
        help_text="Education level"
    )
    
    work_style = serializers.CharField(
        max_length=100,
        help_text="Preferred work style"
    )
    
    def validate_skills(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Please select at least 3 skills")
        
        if len(value) > 20:
            raise serializers.ValidationError("Maximum 20 skills allowed")
        
        return value
    
    def validate_interests(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Please select at least 2 interests")
        
        if len(value) > 10:
            raise serializers.ValidationError("Maximum 10 interests allowed")
        
        return value


class RecommendationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recommendation
        fields = [
            'id',
            'career_name',
            'match_score',
            'confidence_level',
            'rank',
            'matching_skills',
            'missing_skills',
            'completeness_percent',
            'rationale',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class AssessmentSerializer(serializers.ModelSerializer):
    recommendations = RecommendationSerializer(many=True, read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Assessment
        fields = [
            'id',
            'username',
            'skills',
            'interests',
            'education_level',
            'work_style',
            'created_at',
            'updated_at',
            'recommendations'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class AssessmentListSerializer(serializers.ModelSerializer):
    
    top_recommendation = serializers.SerializerMethodField()
    recommendations_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Assessment
        fields = [
            'id',
            'skills',
            'interests',
            'education_level',
            'work_style',
            'created_at',
            'top_recommendation',
            'recommendations_count'
        ]
    
    def get_top_recommendation(self, obj):
        top_rec = obj.recommendations.filter(rank=1).first()
        if top_rec:
            return {
                'career_name': top_rec.career_name,
                'match_score': float(top_rec.match_score)
            }
        return None
    
    def get_recommendations_count(self, obj):
        return obj.recommendations.count()


class CareerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerDetail
        fields = [
            'id',
            'career_name',
            'description',
            'requirements',
            'salary_info',
            'job_growth',
            'work_environment',
            'learning_resources',
            'related_careers',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
