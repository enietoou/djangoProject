
from django.contrib import admin
from django.urls import path
from mainapp.views import home, demand, geography, skills, recent_vacancies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('demand/', demand, name='demand'),
    path('geography/', geography, name='geography'),
    path('skills/', skills, name='skills'),
    path('recent_vacancies/', recent_vacancies, name='recent_vacancies'),
]
