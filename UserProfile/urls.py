from django.urls import path
from UserProfile import views

app_name = 'userprofile'

urlpatterns = [
    path('<int:pk>',views.ProfileDetailView.as_view(),name='ProfileDetail'),
    path('<int:pk>/edit',views.ProfileEditView.as_view(),name='ProfileEdit')
]