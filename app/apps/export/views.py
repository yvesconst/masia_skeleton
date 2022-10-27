from django.shortcuts import render
from django.http import JsonResponse
from jira import JIRA
import json

# Create your views here.

def jira_projects(request):
    jira = JIRA(server="https://jira.atlassian.com")
    #token = """"""
    #jira = JIRA(server="http://localhost:8083", basic_auth=('yvesconst', 'Takianpi1'))

    projects = jira.projects()
    proj = [{'id': p.id, 'name': p.name} for p in projects]
    return JsonResponse({'projects': proj})