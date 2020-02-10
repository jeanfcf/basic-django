from django.shortcuts import render
from post.models import Post
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from post.forms import CreatePostForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'Post/posts.html'


class PostCreateView(LoginRequiredMixin,generic.CreateView):
    model = Post
    template_name = 'Post/createPost.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('post:listaposts')

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'Post/delete.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('post:listaposts')

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ['autor','conteudo','imagem']
    template_name = 'Post/update.html'
    success_url = reverse_lazy('post:listaposts')


