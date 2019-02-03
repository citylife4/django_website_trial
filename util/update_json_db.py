import subprocess
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
from django.core.management import execute_from_command_line
execute_from_command_line('h')
from proj_labels.models import Project, Label

projects_db = Project.objects.all()
labels_db = Label.objects.all()
projects_json = json.load(open('../util/proj_labels.json'))
print(projects_db)
print(projects_json)

print("Parsing the db with jason information")
for project_json, labels_json in projects_json.items():
    print("Parsing following project: ", project_json)
    project_result = Project.objects.filter(project_name=project_json)

    # Include the project if not available
    if not project_result:
        print("Creating new Project: ", project_json)
        new_project = Project(project_name=project_json)
        new_project.save()

    # Hope there is only one
    for project_object in project_result:
        # TODO: check if empty
        print(project_object.label_set.all())



