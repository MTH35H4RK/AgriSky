from django import forms
from django.forms import ModelForm
from .models import CUser, Drone
import os

def custom_upload_to(instance, filename):
			extension = filename.split('.')[-1]
			filename = '{0}.{1}'.format(instance, extension)
			full_path = os.path.join('newstuff/static/images/avatar/', filename)
			if os.path.exists(full_path):
				os.remove(full_path)  
			return 'newstuff/static/images/avatar/{0}'.format(filename)

class CreateUserForm(ModelForm):
	class Meta:
		model = CUser
		fields = ('username', 'password', 'displayname', 'first_name', 'last_name', 'email', 'title', 'avatar', 'userbg')
		labels = {
			'username': '',
			'password': '',
			'displayname': '',
			'first_name': '',
			'last_name': '',
			'email': '',
			'title': '',
			'avatar': '',
			'userbg': '',			
		}
		USERBG_CHOICES = [
			('default', 'Default'),
			('stars', 'Stars'),
		]
		widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
			'password': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}),
			'displayname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Display Name'}),
			'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
			'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
		}
		
		
		avatar = forms.ImageField()
		userbg = forms.ChoiceField(choices=USERBG_CHOICES)

	def save(self, commit=True):
		instance = super(CreateUserForm, self).save(commit=False)
			
		# Handle image upload
		if self.cleaned_data.get('avatar'):
			avatar = self.cleaned_data['avatar']
				
			# Use the custom upload function to determine the path
			upload_path = custom_upload_to(instance.username, avatar.name)
				
			# Save the file to the custom path
			instance.avatar.save(upload_path, avatar, save=False)
			
		if commit:
			instance.save()
		return instance

class UpdateUserForm(ModelForm):
	class Meta:
		model = CUser
		fields = ('displayname', 'first_name', 'last_name', 'email', 'title', 'avatar', 'userbg')
		labels = {
			'displayname': '',
			'first_name': '',
			'last_name': '',
			'email': '',
			'title': '',
			'avatar': '',
			'userbg': '',			
		}
		USERBG_CHOICES = [
			('default', 'Default'),
			('stars', 'Stars'),
		]
		
		
		#avatar = forms.ImageField(path=custom_upload_to)
		userbg = forms.ChoiceField(choices=USERBG_CHOICES,widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Profile Background'}))
		widgets = {
			'displayname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Display Name'}),
			'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
			'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
		}

class CreateDroneForm(ModelForm):
	class Meta:
		model = Drone
		fields = ('dronename', 'location', 'battiere', 'url', 'active')
		labels = {
			'dronename': '',
			'location': '',
			'battiere': '',
			'url': '',
			'active': '',		
		}
		url= forms.URLField(widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Drone Url Feed'}))
		userbg = forms.BooleanField(widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Active'}))
		widgets = {
            'dronename': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dronename'}),
			'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
			'battiere': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Battiere'}),
		}

class UpdateDroneForm(ModelForm):
	class Meta:
		model = Drone
		fields = ('dronename', 'location', 'battiere', 'url', 'active')
		labels = {
			'dronename': '',
			'location': '',
			'battiere': '',
			'url': '',
			'active': '',		
		}
		url= forms.URLField(widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Drone Url Feed'}))
		userbg = forms.BooleanField(widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Active'}))
		widgets = {
            'dronename': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dronename'}),
			'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location'}),
			'battiere': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Battiere'}),
		}