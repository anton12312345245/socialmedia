from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import DetailView,UpdateView,CreateView,ListView,View
from .models import Chat,Message
from django.urls import reverse_lazy
from UserProfile import Profile


class ChatList(ListView):
    model = Chat
    template_name = 'chat/ChatList.html'
    context_object_name = 'chats'
    
    def get_queryset(self):
        return self.request.user.UserProfile.get().chats.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curent_profile = self.request.user.UserProfile.get()
        chatsinfo = []
        for chat in context['chats']:
            otheruser = chat.participants.exclude(pk=curent_profile.pk).first()
            chatsinfo.append({'chat':chat,'otheruser':otheruser})
        context['chatsinfo'] = chatsinfo
        return context
    

class ChatDetail(DetailView):
    model = Chat
    template_name = 'chat/ChatDetail.html'
    context_object_name = 'chat'

    def get_object(self):
        currentprofile = self.request.user.UserProfile.get()
        otherprofile = get_object_or_404(Profile,pk=self.kwargs['ProfileID'])
        chat = Chat.objects.filter(participants=currentprofile).filter(participants=otherprofile).first()
        if not chat:
            chat = Chat.objects.create()
            chat.participants.add(currentprofile,otherprofile)
        return chat