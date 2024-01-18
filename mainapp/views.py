from django.shortcuts import render
from mainapp.scripts.hh_api import get_vacancies_from_hh_api
import requests

from django.views import View
from django.http import JsonResponse
from mainapp.models import Section


def home(request):
    return render(request, 'home.html')


def get_sections(request):
    sections = Section.objects.filter(site_section__url_path=request.path)
    page_name = sections[0].site_section.name
    data = []
    for section in sections:
        with open(section.content.html_table_path.path, 'r') as f:
            html = f.read()
            data.append({'section': section,
                         'html': html,
                         'graph_image_path': '/'.join(section.content.graph_image_path.path.split("/")[-2:])})
    return render(request, 'site_section.html', {'data': data, 'page_name': page_name})


def geography(request):
    sections = Section.objects.filter(site_section__url_path=request.path)
    return render(request, 'geography.html', {'sections': sections})


def skills(request):
    sections = Section.objects.filter(site_section__url_path=request.path)
    return render(request, 'skills.html', {'sections': sections})




def recent_vacancies(request):
    profession = "python-программист"

    data = get_vacancies_from_hh_api(profession)

    if data is not None:
        return render(request, 'recent_vacancies.html', {'vacancies_data': data})
    else:
        return JsonResponse({"error": "Failed to fetch data from HH API"}, status=500)