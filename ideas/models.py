from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.timezone import now

class CustomUser(AbstractUser):
	def __str__(self):
		return self.username

class Idea(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	idea_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	pub_date = models.DateTimeField(default = now)
	
	def __str__(self):
		return self.idea_text
    
