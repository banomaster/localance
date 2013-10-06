from django import forms
from freelancers.tutors.models import Tutor

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        exclude = ('name','slug','featured_in_category','category',)