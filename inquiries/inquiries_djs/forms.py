from django import forms
from .models import InquiryDJ

class InquiryDJForm(forms.ModelForm):
	date = forms.DateField(input_formats=['%d/%m/%Y'])

	class Meta:
		model = InquiryDJ
		exclude = ('user','freelancer','object_id',)
