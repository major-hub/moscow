from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Gallery, News, Question, Contact


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(TranslatableAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(TranslatableAdmin):
    pass
