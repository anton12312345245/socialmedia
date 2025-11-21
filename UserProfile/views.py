from django.shortcuts import render,redirect
from django.views.generic import DetailView,UpdateView,CreateView,ListView,View
from .models import Profile,Follow
from django.urls import reverse_lazy
from .forms import ProfileForm,RegForm
from django.contrib.auth.views import LoginView,LogoutView
from django.db.models import Q

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

    def get_queryset(self):
        getusername = self.request.GET.get('username')
        if getusername:
            return Profile.objects.filter(Q(nickname__icontains=getusername)|Q(user__username__icontains=getusername)).exclude(pk=self.request.user.UserProfile.get().pk)
        else:
            return Profile.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_profile = self.request.user.UserProfile.get()
        context['current_profile'] = current_profile
        profiles = context['profiles']
        profiles_id = [p.id for p in profiles]
        followed_profiles = Follow.objects.filter(follower=current_profile,following__id__in=profiles_id).values_list('following__id',flat=True)
        for profile in profiles:
            profile.isfollowed = profile.id in followed_profiles
        return context


class FollowView(View):
    def get(self,request,pk):
        profiletofollow = Profile.objects.get(pk=pk)
        currentprofile = request.user.UserProfile.get()
        if not Follow.objects.filter(follower=currentprofile,following=profiletofollow).exists():
            Follow.objects.create(follower=currentprofile,following=profiletofollow)
        return redirect('userprofile:SearchFriends')

class UnfollowView(View):
    def get(self,request,pk):
        profiletounfollow = Profile.objects.get(pk=pk)
        currentprofile = request.user.UserProfile.get()
        Follow.objects.filter(follower=currentprofile,following=profiletounfollow).delete()
        return redirect('userprofile:SearchFriends')
       

class FollowersListView(DetailView):
    model = Profile
    template_name = 'UserProfile/followers_list.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['followers_list'] = self.object.followers.all()  # ті, хто підписаний на профіль
        return context


class FollowingListView(DetailView):
    model = Profile
    template_name = 'UserProfile/following_list.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['following_list'] = self.object.following.all()  # на кого підписаний профіль
        return context