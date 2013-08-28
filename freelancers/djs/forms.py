from django import forms
from freelancers.djs.models import DJ

class DJForm(forms.ModelForm):
    class Meta:
        model = DJ
        exclude = ('slug','featured_in_category','category',)