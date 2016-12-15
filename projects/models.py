from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, related_name="projects")
    goal = models.CharField(max_length=140,default=1)
    publish = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to="projects/images", blank=True, null=True)

    def __str__(self):
        return self.name

class Comments(models.Model):
    user = models.ForeignKey(User, related_name='comments')
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Image(models.Model):
    img = models.ImageField(upload_to="projects/images")
    project = models.ForeignKey(Project,related_name="images")
