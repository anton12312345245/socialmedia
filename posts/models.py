from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    content = models.TextField()
    IorV = [('Image', 'Фото'),('Video','Видео')]
    mediatype = models.CharField(choices=IorV,blank=True)
    mediafile = models.FileField(upload_to='posts/media/',null=True,blank=True)
    link = models.URLField(null=True,blank=True)
    created_time = models.DateField(auto_now_add=True)
    
    @property
    def is_image(self):
        return self.mediatype == 'Image'
    @property
    def is_video(self):
        return self.mediatype == 'Video'
    
    def __str__(self):
        return f'{self.author.username}: {self.content[0:50]}'
    

class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')
    comment = models.CharField(max_length=256)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} PostID:{self.post.id} Text:{self.comment[0:50]}'
    

class Likes(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='likes')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} liked: PostID {self.post.id}'
    