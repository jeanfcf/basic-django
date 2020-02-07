from django.contrib.auth.forms import UserCreationForm
from post.models import Post
from django import forms

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['autor','conteudo','imagem']
