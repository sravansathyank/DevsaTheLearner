from django.contrib import admin
from .models import SectorContent

@admin.register(SectorContent)
class SectorContentAdmin(admin.ModelAdmin):
    list_display = ('sector', 'title')
    search_fields = ('sector', 'title')
