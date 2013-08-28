from django import forms
from freelancers.tutors.models import Tutor

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        exclude = ('slug','featured_in_category','category',)