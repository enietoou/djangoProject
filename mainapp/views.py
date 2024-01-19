from django.shortcuts import render
from mainapp.scripts.hh_api import get_vacancies_from_hh_api

from django.views import View
from django.http import JsonResponse
from mainapp.models import Section, SiteSection


def home(request):
    site_sections = SiteSection.objects.all()
    return render(request, 'home.html', {'site_sections': site_sections})


def get_sections(request):
    sections = Section.objects.filter(site_section__url_path=request.path)
    site_sections = SiteSection.objects.all()
    page_name = SiteSection.objects.filter(url_path=request.path)[0].name
    data = []
    for section in sections:
        with open(section.content.html_table_path.path, 'r') as f:
            html = f.read()
            data.append({'section': section,
                         'html': html,
                         'graph_image_path': '/'.join(section.content.graph_image_path.path.split("/")[-2:])})
    return render(request, 'site_section.html', {'data': data,
                                                 'page_name': page_name,
                                                 'site_sections': site_sections})



def recent_vacancies(request):
    site_sections = SiteSection.objects.all()

    profession = "python-программист"

    data = get_vacancies_from_hh_api(profession)

    if data is not None:
        return render(request, 'recent_vacancies.html', {'vacancies_data': data,
                                                         'site_sections': site_sections})
    else:
        return JsonResponse({"error": "Failed to fetch data from HH API"}, status=500)