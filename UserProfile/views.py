from django.shortcuts import render,redirect
from django.views.generic import DetailView,UpdateView
from .models import Profile
from django.urls import reverse_lazy
from .forms import ProfileForm

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'UserProfile/userprofile_detail.html'
    context_object_name = 'UserProfile'
        

class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'UserProfile/editprofile.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('ProfileDetail',kwargs={'pk':self.object.pk})
    

