from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail

from .models import CustomUser

from pprint import pprint

@receiver(post_save, sender=CustomUser)
def acc_creation_email_handler(sender, **kwargs):
	#import pdb; pdb.set_trace()
	user = kwargs.get('instance', None)
	if user is not None:
		subject = "New account creation"
		message = "Welcome %s to Spotlight Ideas! Your account has been created" %user.first_name
		host = settings.EMAIL_HOST_USER
		recipient = [user.email,]
		
		return send_mail(subject, message, host, recipient)
