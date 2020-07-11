from django.contrib import admin
from .models import Profile, UserProduct

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'loyal_point']
    list_display_links = ['user']

admin.site.register(Profile, ProfileAdmin)

admin.site.register(UserProduct)