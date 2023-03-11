from django.contrib import admin

# Register your models here.

from .models import Downloader


admin.site.register(Downloader)
