from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['avatar','bio','nickname','birthday']
        widgets = {'birthday':forms.DateInput(attrs={'type':'date'})}
        

class RegForm(UserCreationForm):
    nickname = forms.CharField(max_length=20,required=True)
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    bio = forms.CharField(max_length=100)

    def save(self,commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            if not Profile.objects.filter(user=user).exists():
                Profile.objects.create(user=user,bio=self.cleaned_data['bio'],birthday=self.cleaned_data['birthday'],nickname=self.cleaned_data['nickname'])
        return user
    
    class Meta():
        model = User
        fields = ['username','email','password1','password2','nickname','birthday','bio']
        


