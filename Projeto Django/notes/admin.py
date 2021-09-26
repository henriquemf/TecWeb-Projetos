from django.contrib import admin
from .models import Note, Tags


admin.site.register(Note)
admin.site.register(Tags)