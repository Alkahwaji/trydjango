from django import forms
from django.core.exceptions import ValidationError

from .models import Product

class PureDjangoForm(forms.Form):
	title           = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Title'}))
	description     = forms.CharField(
									required = False,
									widget = forms.Textarea(
										attrs={
											'placeholder':'Your description',
											'class': 'new-class-name two',
											'id':'my-id-for-textarea',
											'col':120,
										}
										)
									)
	price           = forms.DecimalField()

	#Validation function >> inside the form class
	def clean_title(self, *args, **kwargs): #clean_FieldName
		title = self.cleaned_data['title'] #OR get('FieldName')
		if 'CFE' not in title: #not in allow to write several validations
			raise ValidationError('CFE not involved') #must import validation error
		else:
			return title
			

class ProductionForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['title', 'description','price']


	#Validation function >> inside the form class
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get('title')
		if 'CFE' in title:
			return title
		else:
			raise forms.ValidationError('This is not a valid title')
