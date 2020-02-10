from django.shortcuts import render
from usuario.models import User
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from usuario.forms import CreateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


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
    context_object_name = 'delete'
    success_url = reverse_lazy('usuario:lista')

class UserUpdateView(UpdateView):
    model = User
    fields = ['username','email','password']
    template_name = 'Usuario/update.html'
    success_url = reverse_lazy('usuario:lista')

class UserDetailView(DetailView):
    model = User
    template_name = 'Usuario/detalhes.html'
    context_object_name = 'user'

class UserLoginView(LoginView):
    template_name = 'Usuario/login.html'

class UserLogoutView(LoginRequiredMixin,LogoutView):
    pass 
