from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Experience, Project
from main.permissions import (
    IsPortfolioOwnerOrEditorReadOnly,
    IsPortfolioOwnerOrReadOnly,
)
from main.serializers import ExperienceSerializer, ProjectSerializer


# ==========================================
# 1. PROJECT API VIEWS (Tutorial 07 Utama)
# ==========================================

@api_view(['GET', 'POST'])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def project_list(request):
    if request.method == 'GET':
        title_query = request.GET.get('title', '').strip()
        projects = Project.objects.all()
        if title_query:
            projects = projects.filter(title__icontains=title_query)
            
        serializer = ProjectSerializer(projects, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsPortfolioOwnerOrReadOnly])
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'GET':
        serializer = ProjectSerializer(project, context={'request': request})
        return Response(serializer.data)

    elif request.method in ('PUT', 'PATCH'):
        partial = request.method == 'PATCH'
        serializer = ProjectSerializer(
            project, 
            data=request.data, 
            partial=partial, 
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def project_star(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user in project.starred_by.all():
        project.starred_by.remove(request.user)
    else:
        project.starred_by.add(request.user)
        
    serializer = ProjectSerializer(project, context={'request': request})
    return Response(serializer.data)


# ==========================================
# 2. EXPERIENCE API VIEWS (Tugas Modul)
# ==========================================

@api_view(['GET', 'POST'])
@permission_classes([IsPortfolioOwnerOrEditorReadOnly])
def experience_list(request):
    if request.method == 'GET':
        title_query = request.GET.get('title', '').strip()
        experiences = Experience.objects.all()
        if title_query:
            experiences = experiences.filter(title__icontains=title_query)
            
        serializer = ExperienceSerializer(experiences, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ExperienceSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsPortfolioOwnerOrEditorReadOnly])
def experience_detail(request, pk):
    experience = get_object_or_404(Experience, pk=pk)

    if request.method == 'GET':
        serializer = ExperienceSerializer(experience, context={'request': request})
        return Response(serializer.data)

    elif request.method in ('PUT', 'PATCH'):
        partial = request.method == 'PATCH'
        serializer = ExperienceSerializer(
            experience, 
            data=request.data, 
            partial=partial, 
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def experience_star(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    if request.user in experience.stars.all():
        experience.stars.remove(request.user)
    else:
        experience.stars.add(request.user)
        
    serializer = ExperienceSerializer(experience, context={'request': request})
    return Response(serializer.data)