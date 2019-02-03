# Generated by Django 2.1.5 on 2019-02-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_labels', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='label',
            name='project',
        ),
        migrations.AddField(
            model_name='label',
            name='project',
            field=models.ManyToManyField(to='proj_labels.Project'),
        ),
    ]