from django.shortcuts import render
from usuario.models import User
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from usuario.forms import CreateUserForm
from django.urls import reverse_lazy

# Create your views here.

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'Usuario/usuario.html'

class UserCreateView(CreateView):
    model = User
    template_name = 'Usuario/create.html'
    form_class = CreateUserForm
    success_url = reverse_lazy('usuario:lista')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'Usuario/delete.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('usuario:lista')

class UserUpdateView(UpdateView):
    model = User
    fields = ['username','email','password']
    template_name = 'Usuario/update.html'
    success_url = reverse_lazy('usuario:lista')