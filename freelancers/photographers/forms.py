from django import forms
from freelancers.photographers.models import Photographer

class PhotographerForm(forms.ModelForm):

	class Meta:
		model = Photographer
		exclude = ('name','slug','featured_in_category','category',)
