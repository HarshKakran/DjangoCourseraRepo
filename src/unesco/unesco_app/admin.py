from django.contrib import admin
from .models import Category, ISO, Region, State, Site

# Register your models here.
admin.register(Category)
admin.register(ISO)
admin.register(Region)
admin.register(State)
admin.register(Site)