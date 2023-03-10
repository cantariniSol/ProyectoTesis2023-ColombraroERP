from django.db import models
from django.forms import model_to_dict
from django.contrib.auth.models import AbstractUser

from ColombraroConfig.settings import MEDIA_URL, STATIC_URL

# Create your models here.


class User(AbstractUser):
    imagen = models.ImageField(
        upload_to='users/', null=True,  blank=True, verbose_name='Imágen')

    def get_imagen(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty/empty.png')

    def toJSON(self):
        item = model_to_dict(
            self, exclude=['password', 'user_permissions', 'last_login'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['imagen'] = self.get_imagen()
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name}
                          for g in self.groups.all()]
        return item
