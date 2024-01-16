from django.shortcuts import render

import requests
from django.views import View
from django.http import JsonResponse
# Create your views here.


def home(request):
    return render(request, 'home.html')


def demand(request):
    return render(request, 'demand.html')


def geography(request):
    return render(request, 'geography.html')


def skills(request):
    return render(request, 'skills.html')


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