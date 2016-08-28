from django.contrib import admin
from models import *


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Event, EventAdmin)
