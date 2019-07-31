from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    # meta is used to tell django which model to use for this form
    class Meta:
        model = Post
        fields = ('title', 'text',)