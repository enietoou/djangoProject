
from django.contrib import admin
from django.urls import path
from mainapp.views import home, get_sections, recent_vacancies

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('demand/', get_sections, name='demand'),
    path('geography/', get_sections, name='geography'),
    path('skills/', get_sections, name='skills'),
    path('recent_vacancies/', recent_vacancies, name='recent_vacancies'),
]
