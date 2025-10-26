from django.shortcuts import render,redirect
from django.views.generic import DetailView,UpdateView,CreateView,ListView
from .models import Profile
from django.urls import reverse_lazy
from .forms import ProfileForm,RegForm
from django.contrib.auth.views import LoginView,LogoutView


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
    


class UserRegView(CreateView):
    template_name = 'UserProfile/Reg.html'
    form_class = RegForm

    def get_success_url(self):
        # userprofile = self.request.user.UserProfile.get()
        return reverse_lazy('userprofile:UserLogin')
        

class UserLoginView(LoginView):
    template_name = 'UserProfile/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        userprofile = self.request.user.UserProfile.get()
        return reverse_lazy('userprofile:ProfileDetail',kwargs={'pk':userprofile.pk})
        
    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('userprofile:UserLogin')


class ProfileListView(ListView):
    model = Profile
    template_name = 'UserProfile/searchfriends.html'
    context_object_name = 'profiles'

    