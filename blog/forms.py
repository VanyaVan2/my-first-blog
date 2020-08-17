from django import forms
from .models import Post, Task

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
        