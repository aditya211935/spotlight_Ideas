from pprint import pprint
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from social_core.pipeline.partial import partial
USER_FIELDS = ['username', 'email']

@partial
def display(strategy, details, backend, user=None, *args, **kwargs):
	#import pdb; pdb.set_trace()
	if not user and (not details['email'] or not details['first_name'] or not details['last_name']):
		new_details = strategy.session_get('new_details', None)
		if new_details is None or (not new_details['email'] or not new_details['first_name'] or not new_details['last_name']):
			strategy.session['new_details'] = details
			return HttpResponseRedirect(reverse('ideas:add_info'))
		else:
			details.update(new_details)
	return
	
	"""
	print('=' * 80)
	pprint(strategy.request_data())
	print('=' * 80)
	pprint(details)
	print('=/' * 80)
	fields = dict((name, kwargs.get(name, details.get(name)))
				for name in backend.setting('USER_FIELDS', USER_FIELDS))
	pprint(fields)
	print('=/' * 80)
	pprint(user)
	print('=' * 80)
	pprint(args)
	print('=' * 80)
	pprint(kwargs)
	"""
	
