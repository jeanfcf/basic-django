from django.urls import path
from usuario.views import UserListView,UserCreateView,UserDeleteView,UserUpdateView,UserDetailView,UserLoginView,UserLogoutView

app_name = 'usuario'

urlpatterns = [
   path('usuario',UserListView.as_view(),name="lista"),
   path('criarusuario',UserCreateView.as_view(),name="criar"),
   path('usuario/<int:pk>/apagar',UserDeleteView.as_view(),name="deletaruser"),
   path('usuario/<int:pk>/update',UserUpdateView.as_view(),name="updateuser"),
   path('usuario/<int:pk>/detalhes',UserDetailView.as_view(),name="detalhesuser"),
   path('usuario/login',UserLoginView.as_view(),name="loginuser"),
   path('usuario/logout',UserLogoutView.as_view(),name="logoutuser"),
   

]