
from django.db import models
from django.conf import settings
from django.utils import timezone


class Assessment(models.Model):
    
    # Link to User model (ForeignKey = One-to-Many)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # References our CustomUser
        on_delete=models.CASCADE,   # If user deleted, delete their assessments
        related_name='assessments'  # Access user's assessments: user.assessments.all()
    )
    
    # Skills - stored as JSON array
    # Example: ["Programming", "Data Analysis", "Design"]
    skills = models.JSONField(
        help_text="List of user's skills"
    )
    
    # Interests - stored as JSON array
    # Example: ["Technology & Innovation", "Arts & Design"]
    interests = models.JSONField(
        help_text="List of user's interests"
    )
    
    # Education level - single choice
    education_level = models.CharField(
        max_length=100,
        help_text="User's education level"
    )
    
    # Work style preference - single choice
    work_style = models.CharField(
        max_length=100,
        help_text="Preferred work environment"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name = 'Assessment'
        verbose_name_plural = 'Assessments'
    
    def __str__(self):
        return f"Assessment by {self.user.username} on {self.created_at.strftime('%Y-%m-%d')}"


class Recommendation(models.Model):
    
    # Link to Assessment (ForeignKey)
    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.CASCADE,  # If assessment deleted, delete recommendations
        related_name='recommendations'
    )
    
    # Career information
    career_name = models.CharField(
        max_length=200,
        help_text="Name of the recommended career"
    )
    
    # ML model output
    match_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Match percentage (0-100)"
    )
    
    confidence_level = models.CharField(
        max_length=20,
        choices=[
            ('Very High', 'Very High'),
            ('High', 'High'),
            ('Moderate', 'Moderate'),
            ('Low', 'Low'),
        ],
        help_text="Confidence level of recommendation"
    )
    
    rank = models.IntegerField(
        help_text="Rank in top 5 (1-5)"
    )
    
    # Skill gap analysis - stored as JSON
    matching_skills = models.JSONField(
        help_text="Skills user has that match this career"
    )
    
    missing_skills = models.JSONField(
        help_text="Skills user needs to learn for this career"
    )
    
    completeness_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Skill completeness percentage"
    )
    
    # Full rationale - stored as JSON for flexibility
    rationale = models.JSONField(
        blank=True,
        null=True,
        help_text="Detailed explanation of recommendation"
    )
    
    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['assessment', 'rank']  # Order by assessment, then rank
        verbose_name = 'Recommendation'
        verbose_name_plural = 'Recommendations'
    
    def __str__(self):
        return f"#{self.rank} {self.career_name} ({self.match_score}%)"


class CareerDetail(models.Model):
    career_name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Career title"
    )
    
    description = models.TextField(
        help_text="What this career involves"
    )
    
    # Requirements stored as JSON
    requirements = models.JSONField(
        help_text="Education, skills, certifications needed"
    )
    
    # Salary information
    salary_info = models.JSONField(
        help_text="Entry, mid, senior level salary ranges"
    )
    
    job_growth = models.CharField(
        max_length=100,
        help_text="Job market growth outlook"
    )
    
    work_environment = models.TextField(
        blank=True,
        help_text="Typical work setting and conditions"
    )
    
    # Learning resources
    learning_resources = models.JSONField(
        blank=True,
        null=True,
        help_text="Courses, books, websites for learning"
    )
    
    # Related careers
    related_careers = models.JSONField(
        blank=True,
        null=True,
        help_text="Similar or related career paths"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['career_name']
        verbose_name = 'Career Detail'
        verbose_name_plural = 'Career Details'
    
    def __str__(self):
        return self.career_name

