from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import CustomUser, Idea


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
	last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	username = forms.CharField(max_length=30, required=True, help_text='Required.')
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email', 'password')

class AddIdeaForm(forms.ModelForm):
	class Meta:
		model = Idea
		fields = ('idea_text',)
		
class emailReqdForm(forms.Form):
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
	last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
