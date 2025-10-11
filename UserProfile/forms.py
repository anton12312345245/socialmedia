from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['avatar','bio','nickname','birthday']
        widgets = {'birthday':forms.DateInput(attrs={'type':'date'})}
        