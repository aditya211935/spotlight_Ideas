from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy, reverse

from pprint import pprint

from .forms import SignUpForm,AddIdeaForm,emailReqdForm
from .models import Idea, CustomUser

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect(reverse('ideas:ideas_home'))
	else:
		form = SignUpForm()
	return render(request, 'ideas/signup.html', {'form': form})

@login_required(login_url=reverse_lazy('ideas:login'))
def ideas_view(request):
	ideas_list = Idea.objects.order_by('-pub_date')
	return render(request, 'ideas/ideas_list.html', {'ideas_list': ideas_list})

@login_required(login_url=reverse_lazy('ideas:login'))	
def detail(request, idea_id):
	idea = get_object_or_404(Idea, pk=idea_id)
	return render(request, 'ideas/detail.html', {'idea': idea})

@login_required(login_url=reverse_lazy('ideas:login'))	
def add_idea(request):
	#import pdb; pdb.set_trace()
	if request.method == 'POST':
		form = AddIdeaForm(request.POST)
		#import pdb; pdb.set_trace()
		if form.is_valid():
			#create idea object, populate time, user, idea_text
			idea_text = form.cleaned_data.get('idea_text')
			user = CustomUser.objects.get(username=request.user)
			Idea.objects.create(user=request.user, idea_text=idea_text)
			x = HttpResponseRedirect(reverse('ideas:ideas_home'))
			pprint(x)
			return x
	else:
		form = AddIdeaForm()
	return render(request, 'ideas/add_idea.html', {'form': form})
	
@login_required(login_url=reverse_lazy('ideas:login'))		
def change_idea(request, idea_id):
	idea = get_object_or_404(Idea, pk=idea_id)
	if idea.user == request.user:
		if request.method == 'POST':
			form = AddIdeaForm(request.POST)
			if form.is_valid():
				idea.idea_text = form.cleaned_data.get('idea_text')
				idea.save()
				return HttpResponseRedirect(reverse('ideas:ideas_home'))
		else:
			form = AddIdeaForm(instance=idea)
		return render(request, 'ideas/change_idea.html', {'form': form})
	else:
		return render(request, 'ideas/detail.html', {
			'idea': idea,
			'error_message': "Sorry! You're not authorized for this."
		})
		
@login_required(login_url=reverse_lazy('ideas:login'))			
def delete_idea(request, idea_id):
	idea = get_object_or_404(Idea, pk=idea_id)
	if idea.user == request.user:
		idea.delete()
		return HttpResponseRedirect(reverse('ideas:ideas_home'))
	else:
		return render(request, 'ideas/detail.html', {
			'idea': idea,
			'error_message': "Sorry! You're not authorized for this."
		})

@login_required(login_url=reverse_lazy('ideas:login'))		
def upvote(request, idea_id):
	idea = get_object_or_404(Idea, pk=idea_id)
	idea.votes += 1
	idea.save()
	return HttpResponseRedirect(reverse('ideas:detail', args=(idea_id,)))

@login_required(login_url=reverse_lazy('ideas:login'))		
def downvote(request, idea_id):
	idea = get_object_or_404(Idea, pk=idea_id)
	idea.votes -= 1
	idea.save()
	return HttpResponseRedirect(reverse('ideas:detail', args=(idea_id,)))

def add_info(request):
	if request.session.get('new_details') is None:
		raise Http404
	if request.method == 'POST':
		form = emailReqdForm(request.POST)
		if form.is_valid():
			request.session['new_details'] = form.cleaned_data
			return HttpResponseRedirect(reverse('social:complete', args=("github",)))		
	else:
		form = emailReqdForm(request.session['new_details'])
	return render(request, "ideas/add_info.html", {'form': form})
			
			
