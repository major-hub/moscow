from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Gallery, News


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    pass
