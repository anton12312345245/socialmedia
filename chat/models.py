from django.db import models
from UserProfile.models import Profile

class Chat(models.Model):
    participants = models.ManyToManyField(Profile,related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)
    last_message = models.DateTimeField(auto_now=True)
    is_group = models.BooleanField(default=False)
    group_name = models.CharField(max_length=100,blank=True,null=True)
    creator = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,related_name='created_groups')
    
    class Meta():
        ordering = ['-last_message']


class Message(models.Model):
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE,related_name='messages')
    sender = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='messages')
    text = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)




