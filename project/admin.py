from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'service', 'technology', 'user', 'is_processed']
    list_display_links = ['name']

admin.site.register(Project, ProjectAdmin)