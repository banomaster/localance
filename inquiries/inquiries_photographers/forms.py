from django import forms
from .models import InquiryPhotographer

class InquiryPhotographerForm(forms.ModelForm):
	date = forms.DateField(input_formats=['%d/%m/%Y'])

	class Meta:
		model = InquiryPhotographer
		exclude = ('user','freelancer','object_id',)


