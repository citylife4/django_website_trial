from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

import json

from .forms import ProjectForm
from .models import Project, Label


def index(request):
    projects = Project.objects.all()
    labels_result = Label.objects.all()
    query = request.GET.get("q")
    if query:
        return render(request, 'proj_labels/index.html', {
            'projects': projects,
            'labels': labels_result,
        })
    else:
        return render(request, 'proj_labels/index.html', {'projects': projects})


def labels(request, filter_by):
    try:
        label_ids = []
        for project in Project.objects.filter(user=request.user):
            for label in project.label_set.all():
                label_ids.append(label.pk)
        users_labels = Label.objects.filter(pk__in=label_ids)
    except Label.DoesNotExist:
        users_labels = []
    return render(request, 'proj_labels/labels.html', {
        'label_list': users_labels,
        'filter_by': filter_by,
    })


def detail(request, project_id):
    user = request.user
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'proj_labels/detail.html', {'project': project})


def create_project(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        project = form.save(commit=False)
        project.user = request.user
        project.project_logo = request.FILES['project_logo']
        project.save()
        return render(request, 'proj_labels/detail.html', {'project': project})
    context = {
        "form": form,
    }
    return render(request, 'proj_labels/create_project.html', context)


def update_database_json(request):
    projects_result = Project.objects.all()
    labels_result = Label.objects.all()
    projects_json = json.load(open('util/proj_labels.json'))
    print(projects_result)
    for project_json in projects_json:
        print(project_json)
        if project_json in projects_result:
            print("include")
            project_toinclude = Project(project_name=project_json)

