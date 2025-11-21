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
    path('follow/<int:pk>',views.FollowView.as_view(),name='FollowProfile'),
    path('unfollow/<int:pk>',views.UnfollowView.as_view(),name='UnfollowProfile'),
    path('<int:pk>/followers/', views.FollowersListView.as_view(), name='followers_list'),
    path('<int:pk>/following/', views.FollowingListView.as_view(), name='following_list'),
]