from django import forms
from .models import InquiryTutor

class InquiryTutorForm(forms.ModelForm):
	date = forms.DateField(input_formats=['%d/%m/%Y'])

	class Meta:
		model = InquiryTutor
		exclude = ('user','freelancer','object_id',)


