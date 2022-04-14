from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class News(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=300),
        content=models.TextField()
    )
    image = models.ImageField(upload_to='news/')
    is_active = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f"{self.pk} - image"


class Question(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=17)
    message = models.TextField()
    is_answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


class Contact(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=17)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
