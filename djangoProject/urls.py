
from django.contrib import admin
from django.urls import path
from mainapp.views import home, demand

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('demand/', demand, name='demand'),
    path('geography/', demand, name='geography'),
]
