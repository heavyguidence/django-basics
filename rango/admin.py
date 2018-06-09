# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rango.models import Category,Page


# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class Categorydmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')

admin.site.register(Category,Categorydmin)
admin.site.register(Page,PageAdmin)

