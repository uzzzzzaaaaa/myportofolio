from main.models import Experience, Project

from django.contrib import messages

from django.core import serializers

from django.http import HttpResponse, HttpResponseForbidden

from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProjectForm, ExperienceForm

from django.contrib.auth import login, logout

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.decorators import login_required

from django.core.exceptions import PermissionDenied

import datetime



def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    is_editor = False
    if request.user.is_authenticated:
        is_editor = request.user.groups.filter(name='Editor').exists()
    context = {
        "name": "Hudzaifah",
        "npm": "2506622840",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer di Universitas Indonesia yang hobi mengotomatiskan segala sesuatu yang bersifat repetitif."
        ),
        "last_login": last_login,
        'is_editor': is_editor,
        
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Hudzaifah",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Burhan",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json", use_natural_foreign_keys=True)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
            raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url='/login/')
def create_experience(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("403 Forbidden: Hanya Pemilik Portofolio yang dapat membuat data.")
    form = ExperienceForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience') 

    context = {'form': form}
    return render(request, "create_experience.html", context)

@login_required(login_url='/login/')
def edit_experience(request, id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    
    if not (request.user.is_superuser or is_editor):
        return HttpResponseForbidden("403 Forbidden: Anda tidak memiliki hak untuk mengubah data.")
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_experience')

    context = {'form': form, 'experience': experience}
    return render(request, "edit_experience.html", context)

@login_required(login_url='/login/')
def delete_experience(request, id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("403 Forbidden: Hanya Pemilik Portofolio yang dapat menghapus data.")
    experience = get_object_or_404(Experience, pk=id)
    experience.delete()
    return redirect('main:show_experience')

def show_json_experience(request):
    data = Experience.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("main:show_main")

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@login_required(login_url='/login/')
def toggle_star_experience(request, id):
    if request.method == 'POST':
        experience = get_object_or_404(Experience, pk=id)
        
        if request.user in experience.stars.all():
            experience.stars.remove(request.user)
        else:
            experience.stars.add(request.user)
            
    return redirect('main:show_experience')