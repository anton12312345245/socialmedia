from django.urls import path
from UserProfile import views

app_name = 'userprofile'

urlpatterns = [
    path('<int:pk>',views.ProfileDetailView.as_view(),name='ProfileDetail'),
    path('<int:pk>/edit',views.ProfileEditView.as_view(),name='ProfileEdit'),
    path('login/',views.UserLoginView.as_view(),name='UserLogin'),
    path('logout/',views.UserLogoutView.as_view(),name='UserLogout'),
    path('Registration/',views.UserRegView.as_view(),name='UserReg'),
    path('search/',views.ProfileListView.as_view(),name='SearchFriends'),
]