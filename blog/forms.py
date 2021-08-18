from django import forms
from .widgets import CustomClearableFileInput
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'blog_content', 'image' )
        exclude = ('user', 'created_on', )

image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment_content',)
