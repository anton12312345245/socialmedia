from django.urls import path
from chat import views

app_name = 'chat'

urlpatterns = [
    path('',views.ChatList.as_view(),name='ChatList'),
    path('<int:ProfileID>/',views.ChatDetail.as_view(),name='ChatDetail'),
]