from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


def phone_number_validator(ph: str):
    ph = ph.replace(' ', '').replace('+', '')
    if not bool(ph.isdigit() and ph.startswith('998') and len(ph) == 12):
        raise ValidationError('Phone number must be like 998911144735')


class CustomUser(AbstractUser):
    username = models.CharField(max_length=17, unique=True, validators=[phone_number_validator])

    def save(self, *args, **kwargs):
        self.username = self.username.replace(' ', '').replace('+', '')
        if not self.password.startswith("pbkdf2_sha256"):
            self.set_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_joined']
