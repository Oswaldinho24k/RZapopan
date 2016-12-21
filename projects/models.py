from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, related_name="projects", blank=True, null=True)
    goal = models.CharField(max_length=140,default=1, blank=True, null=True)
    publish = models.DateTimeField(auto_now=True, blank=True, null=True)
    img = models.ImageField(upload_to="projects/images", blank=True, null=True)
    video = models.CharField(max_length=500, blank=True,null=True)



    def __str__(self):
        return self.name



class Comments(models.Model):
    user = models.ForeignKey(User, related_name='comments')
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Image(models.Model):
    img = models.ImageField(upload_to="projects/images")
    project = models.ForeignKey(Project,related_name="images")

class NewProject(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    goal = models.DecimalField(max_digits=7, decimal_places=2, default=1, blank=True, null=True)
