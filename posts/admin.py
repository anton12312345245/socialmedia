from django.contrib import admin
from .models import Post,Likes,Comments

admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Comments)