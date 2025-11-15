from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView
from .models import Post
from .forms import AddPostForm
from django.urls import reverse_lazy
from UserProfile.models import Profile

class ListPostView(ListView):
    model = Post
    template_name = 'Posts/PostsList.html'
    context_object_name = 'Posts'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            current_profile = self.request.user.UserProfile.get()
            following_profiles = Profile.objects.filter(followers__follower=current_profile)
            return Post.objects.filter(author__UserProfile__in=following_profiles)
        else:
            return Post.objects.all()
         


class CreatePostView(CreateView):
    model = Post
    template_name = 'UserProfile/CreatePost.html'
    form_class = AddPostForm
    success_url = reverse_lazy('userprofile:ProfileDetail',kwargs={'pk':1})

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'UserProfile/DeletePost.html'
    success_url = reverse_lazy('userprofile:ProfileDetail',kwargs={'pk':1})
    
    