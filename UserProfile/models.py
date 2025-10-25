from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='UserProfile')
    avatar = models.ImageField(upload_to='avatars/',null=True,blank=True)
    bio = models.TextField(max_length=256,blank=True,null=True)
    birthday = models.DateField(blank=True,null=True)
    nickname = models.TextField(max_length=20)
    # userposts = models.ForeignKey(Post,blank=True,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'Hello,{self.nickname}'