from django.contrib import admin
from .models import*

# Register your models here.

admin.site.register(NewsCategory)
admin.site.register(CreateNews)
admin.site.register(Comment)
admin.site.register(Profession)