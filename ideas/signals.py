from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail

from .models import CustomUser, Idea

from pprint import pprint

@receiver(post_save, sender=CustomUser)
def acc_creation_email_handler(sender, **kwargs):
	#import pdb; pdb.set_trace()
	created = kwargs.get('created')
	user = kwargs.get('instance', None)
	if user is not None and created:
		subject = "New account creation"
		message = "Welcome %s to Spotlight Ideas! Your account has been created" %user.first_name
		host = settings.EMAIL_HOST_USER
		recipient = [user.email,]
		
		return send_mail(subject, message, host, recipient)
		
@receiver(post_save, sender=Idea)
def idea_creation_email_handler(sender, **kwargs):
	#import pdb; pdb.set_trace()
	created = kwargs.get('created')
	idea = kwargs.get('instance')
	if created:
		subject = "New idea created"
		message = "Hello %s! New idea has been successfully created.\nIdea: %s" % (idea.user.first_name, idea.idea_text)
		host = settings.EMAIL_HOST_USER
		recipient = [idea.user.email,]
		return send_mail(subject, message, host, recipient)
	"""
	else:
		subject = "Idea changed"
		message = "Hello %s! Idea has been successfully changed.\nIdea: %s" % (idea.user.first_name, idea.idea_text)
		host = settings.EMAIL_HOST_USER
		recipient = [idea.user.email,]
		return send_mail(subject, message, host, recipient)
		{'created': True,
	 'instance': <Idea: lolo>,
	 'raw': False,
	 'signal': <django.db.models.signals.ModelSignal object at 0x7fa2c750a7b8>,
	 'update_fields': None,
	 'using': 'default'}
	"""

@receiver(post_delete, sender=Idea)
def idea_deletion_email_handler(sender, **kwargs):
	idea = kwargs.get('instance')
	subject = "Idea deleted"
	message = "Hello %s! Idea has been successfully deleted.\nIdea: %s" % (idea.user.first_name, idea.idea_text)
	host = settings.EMAIL_HOST_USER
	recipient = [idea.user.email,]
	return send_mail(subject, message, host, recipient)
