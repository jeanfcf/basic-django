from django.urls import path
from usuario.views import UserListView,UserCreateView,UserDeleteView,UserUpdateView

app_name = 'usuario'

urlpatterns = [
   path('usuario',UserListView.as_view(),name="lista"),
   path('criarusuario',UserCreateView.as_view(),name="criar"),
   path('usuario/<int:pk>/apagar',UserDeleteView.as_view(),name="deletaruser"),
    path('usuario/<int:pk>/update',UserUpdateView.as_view(),name="updateuser")


]