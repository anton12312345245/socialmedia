from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['content','mediatype','mediafile','link']
        widgets = {
        'content':forms.Textarea(),
        # 'mediatype':forms.ChoiceField(choices=[('Image', 'Фото'),('Video','Видео')],required=False),
        'mediafile':forms.FileInput(),
        'link':forms.URLInput()
                }