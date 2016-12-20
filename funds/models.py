from django.db import models
from django.contrib.auth.models import User
from projects.models import Project


class Fund(models.Model):
	amount = models.CharField(max_length=10)
	contributor = models.ForeignKey(User, related_name='funds')
	project = models.ForeignKey(Project, related_name='funds')
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{} en {} por {}".format(self.amount, self.project, self.contributor)
		

class Chat(models.Model):
	contributor = models.ForeignKey(User, related_name='cchats')
	project = models.ForeignKey(Project, related_name='chats')
	padmin = models.ForeignKey(User, related_name='pchats')
	uid = models.CharField(max_length=140)

	def __str__(self):
		return "chat between {} & {}".format(self.contributor, self.padmin)