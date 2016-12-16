from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    img = models.ImageField(upload_to='profile_img')
    tel = models.CharField(max_length=50)

    def __str__(self):
    	return 'Perfil del usuario {}'.format(self.user.username)


