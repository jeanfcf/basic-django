from django.shortcuts import render
from post.models import Post
from django.views.generic import ListView,CreateView
from post.forms import CreatePostForm
from django.urls import reverse_lazy
# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'Post/posts.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'Post/createPost.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('post:listaposts')
