from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Hudzaifah",
        "npm": "2506622840",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer di Universitas Indonesia yang hobi mengotomatiskan segala sesuatu yang bersifat repetitif."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Hudzaifah",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)