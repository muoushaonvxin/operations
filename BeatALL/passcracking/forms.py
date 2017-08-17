from django import forms
from passcracking import models

class ssh_crack_ModelForm(forms.ModelForm):

	class Meta:
		model = models.ssh_crack
		exclude = ()

		widgets = {
			"host": forms.TextInput(attrs={"class": "host_ip"}),
            "port": forms.TextInput(attrs={"class": "port"}),
            "dictionary": forms.TextInput(attrs={"class": "dictionary"}),
			"user": forms.TextInput(attrs={"class": "user"}),
			"name": forms.TextInput(attrs={"class": "name"}),
			"add_time": forms.TextInput(attrs={"class": "add_time"}),
		}



