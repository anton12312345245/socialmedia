from django.urls import path

from UserProfile import views


urlpatterns = [
    path('<int:pk>',views.ProfileDetailView.as_view(),name='ProfileDetail'),
]