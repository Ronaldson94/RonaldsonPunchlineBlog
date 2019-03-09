from django import forms
from .models import Punchline,Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('auteur','text',)
