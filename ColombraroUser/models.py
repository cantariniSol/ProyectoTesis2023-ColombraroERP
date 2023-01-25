from django.db import models
from django.contrib.auth.models import AbstractUser

from ColombraroConfig.settings import MEDIA_URL, STATIC_URL

# Create your models here.


class User(AbstractUser):
    imagen = models.ImageField(
        upload_to=' users/', null=True,  blank=True)

    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty/empty.png')
