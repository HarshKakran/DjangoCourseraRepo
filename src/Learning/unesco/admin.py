from django.contrib import admin

from .models import Category, ISO, Region, State, Site

# Register your models here.
admin.site.register(ISO)
admin.site.register(Category)
admin.site.register(Region)
admin.site.register(State)
admin.site.register(Site)
