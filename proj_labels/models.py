from django.contrib.auth.models import Permission, User
from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=500)

    def __str__(self):
        return self.project_name


class Label(models.Model):
    project = models.ManyToManyField(Project)
    label_title = models.CharField(max_length=500)
    macro_type = models.CharField(max_length=500)

    def __str__(self):
        return self.label_title + ' - ' + self.macro_type
