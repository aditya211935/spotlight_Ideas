from django.apps import AppConfig


class IdeasConfig(AppConfig):
    name = 'ideas'
    
    def ready(self):
    	import ideas.signals
