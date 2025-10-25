from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView
from .models import Post
from .forms import AddPostForm
from django.urls import reverse_lazy

class ListPostView(ListView):
    model = Post
    template_name = 'Posts/PostsList.html'
    context_object_name = 'Posts'

    # def get_queryset(self):
        # return Post.objects.filter(author=self.request.user).order_by('-created_time')    


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
    
    