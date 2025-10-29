
from django.contrib import admin
from .models import Assessment, Recommendation, CareerDetail


class RecommendationInline(admin.TabularInline):
    model = Recommendation
    extra = 0  # Don't show empty forms
    readonly_fields = ('career_name', 'match_score', 'rank', 'confidence_level')
    fields = ('rank', 'career_name', 'match_score', 'confidence_level')
    can_delete = False


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'user', 'created_at', 'education_level', 'work_style')
    list_filter = ('education_level', 'work_style', 'created_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Assessment Data', {
            'fields': ('skills', 'interests', 'education_level', 'work_style')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapsible section
        }),
    )
    
    inlines = [RecommendationInline]  # Show recommendations on same page
    
    def has_add_permission(self, request):
        """
        Disable manual creation (assessments come from API)
        """
        return False


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('id', 'assessment', 'rank', 'career_name', 'match_score', 'confidence_level')
    list_filter = ('confidence_level', 'created_at')
    search_fields = ('career_name', 'assessment__user__username')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('assessment', 'career_name', 'rank')
        }),
        ('ML Output', {
            'fields': ('match_score', 'confidence_level', 'completeness_percent')
        }),
        ('Skill Analysis', {
            'fields': ('matching_skills', 'missing_skills')
        }),
        ('Additional Data', {
            'fields': ('rationale', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        return False


@admin.register(CareerDetail)
class CareerDetailAdmin(admin.ModelAdmin):
    
    list_display = ('career_name', 'job_growth', 'created_at')
    search_fields = ('career_name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('career_name', 'description', 'work_environment')
        }),
        ('Requirements', {
            'fields': ('requirements',)
        }),
        ('Compensation & Growth', {
            'fields': ('salary_info', 'job_growth')
        }),
        ('Learning Resources', {
            'fields': ('learning_resources', 'related_careers')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


