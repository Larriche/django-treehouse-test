from django.contrib import admin

from .models import Song, Performer


admin.site.register(Song)
admin.site.register(Performer)