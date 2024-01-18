from django.contrib import admin
from .models import SiteSection, StatisticContent, Section

# Register your models here.

admin.site.register(SiteSection)
admin.site.register(StatisticContent)
admin.site.register(Section)