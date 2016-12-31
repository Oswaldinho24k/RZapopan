from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    img = models.ImageField(upload_to='profile_img', blank=True, null=True)
<<<<<<< HEAD
    tel = models.CharField(max_length=50, blank=True, null=True)
=======
    tel = models.CharField(max_length=50,  blank=True, null=True)
>>>>>>> 32f9e519bac767bbaf651c9e42e428e28b77d88d

    def __str__(self):
    	return 'Perfil del usuario {}'.format(self.user.username)


