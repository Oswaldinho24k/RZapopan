from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Input(models.Model):
    user = models.ForeignKey(User, related_name='inputs')
    project = models.ForeignKey(Project, related_name="projects")
    amount = models.DecimalField(decimal_places=2)
    date = models.DateTimeField(auto_now=True)



