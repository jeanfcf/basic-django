from django.urls import path
from usuario.views import UserListView,UserCreateView

app_name = 'usuario'

urlpatterns = [
   path('usuario',UserListView.as_view(),name="lista"),
   path('criarusuario',UserCreateView.as_view(),name="criar"),


]