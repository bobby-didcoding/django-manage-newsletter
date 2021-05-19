from django.forms import ModelForm
from django import forms
from .models import NewsLetter



class NewsLetterForm(forms.ModelForm):

	email = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			}))
	
	class Meta:
		model = NewsLetter
		fields = ('email', )
