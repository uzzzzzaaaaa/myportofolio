from django.urls import path
from main import api_views

app_name = "api"

urlpatterns = [
    # Endpoint Projects
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:pk>/", api_views.project_detail, name="project-detail"),
    path("projects/<uuid:pk>/star/", api_views.project_star, name="project-star"),
    
    # Endpoint Experiences
    path("experiences/", api_views.experience_list, name="experience-list"),
    path("experiences/<uuid:pk>/", api_views.experience_detail, name="experience-detail"),
    path("experiences/<uuid:pk>/star/", api_views.experience_star, name="experience-star"),
]