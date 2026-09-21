from django.urls import path

from main.views import show_main, show_experience, show_projects, create_project, get_projects_json, delete_project

from main.views import create_experience, edit_experience, delete_experience, show_json_experience

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path('projects/', show_projects, name='show_projects'),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path('experience/add/', create_experience, name='create_experience'),
    path('experience/edit/<uuid:id>/', edit_experience, name='edit_experience'),
    path('experience/delete/<uuid:id>/', delete_experience, name='delete_experience'),
    path('json-experience/', show_json_experience, name='show_json_experience'),
]