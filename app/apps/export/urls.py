from django.urls import path, include
from .views import jira_projects

urlpatterns  = [
    path('jira', jira_projects, name='jira-test')
]