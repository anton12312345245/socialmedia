from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class ListPostView(ListView):
    model = Post
    template_name = 'Posts/PostsList.html'
    context_object_name = 'Posts'

    # def get_queryset(self):
        # return Post.objects.filter(author=self.request.user).order_by('-created_time')    


