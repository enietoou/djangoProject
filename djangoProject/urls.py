
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from mainapp.views import home, get_sections, recent_vacancies
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('', home, name='home'),
    path('demand/', get_sections, name='demand'),
    path('geography/', get_sections, name='geography'),
    path('skills/', get_sections, name='skills'),
    path('recent_vacancies/', recent_vacancies, name='recent_vacancies'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)