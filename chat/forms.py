from django import forms
from .models import Chat
from UserProfile.models import Profile

class GroupForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(queryset=None,widget=forms.CheckboxSelectMultiple,label='add people')

    class Meta():
        model = Chat
        fields = ['group_name','participants']

    def __init__(self,user,*args,**kwargs):
        super().__init__(*args,**kwargs)
        current_profile = user.UserProfile.get()
        following_profiles = current_profile.following.values_list('following',flat=True)
        self.fields['participants'].queryset = Profile.objects.filter(pk__in=following_profiles)