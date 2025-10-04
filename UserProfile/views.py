from django.shortcuts import render
from django.views.generic import DetailView,UpdateView
from .models import Profile

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'UserProfile/userprofile_detail.html'
    context_object_name = 'UserProfile'
    