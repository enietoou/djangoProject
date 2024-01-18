from django.shortcuts import render

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
    # hh_api_key = "Ваш_ключ_API_HH"
    profession = "python"

    # Формируем URL запрос
    url = f"https://api.hh.ru/vacancies?text={profession}&period=1&per_page=10&order_by=publication_time&sort_order=desc"

    # Выполняем GET-запрос к API HH
    # response = requests.get(url, headers={"User-Agent": "MainApp", "Authorization": f"Bearer {hh_api_key}"})
    response = requests.get(url, headers={"User-Agent": "MainApp"})

    if response.status_code == 200:
        vacancies_data = response.json()["items"]
        return render(request, 'recent_vacancies.html', {'vacancies_data': vacancies_data})
    else:
        # Обработка ошибок
        return JsonResponse({"error": "Failed to fetch data from HH API"}, status=500)