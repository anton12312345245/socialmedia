from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/images/',null=True,blank=True)
    video = models.FileField(upload_to='posts/videos/',null=True,blank=True)
    link = models.URLField(null=True,blank=True)
    created_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} {self.content[0:50]}'
    

class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} post id {self.post.id} text:{self.comment[0:50]}'
    

class Likes(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} liked: post id {self.post.id}'
    