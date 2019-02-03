from django.conf.urls import url
from . import views

app_name = 'proj_labels'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^labels/(?P<filter_by>[a-zA_Z]+)/$', views.labels, name='labels'),
    url(r'^create_project/$', views.create_project, name='create_project'),
    url(r'^update_database/$', views.update_database_json, name='update_database_json'),

]