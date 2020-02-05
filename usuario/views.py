from django.shortcuts import render
from usuario.models import User
from django.views.generic import ListView

# Create your views here.

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'Usuario/usuario.html'