from django.urls import path
from posts import views

app_name = 'posts'


urlpatterns = [
    path('',views.ListPostView.as_view(),name='ListPostView'),
    path('create/',views.CreatePostView.as_view(),name='CreatePost'),
    path('delete/<int:pk>',views.DeletePostView.as_view(),name='DeletePost'),
]
