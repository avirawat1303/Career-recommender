
from django.urls import path
from . import views

urlpatterns = [
    
    path('assessment/', views.submit_assessment, name='submit_assessment'),
    path('assessment/history/', views.assessment_history, name='assessment_history'),
    path('assessment/<int:id>/', views.assessment_detail, name='assessment_detail'),
    path('careers/', views.career_list, name='career_list'),
    path('careers/<str:name>/', views.career_detail, name='career_detail'),
]