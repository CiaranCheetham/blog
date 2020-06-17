from django import forms
from .models import Post, Comment, CVSection


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class CVForm(forms.ModelForm):

    class Meta:
        model = CVSection
        fields = ('text',)
