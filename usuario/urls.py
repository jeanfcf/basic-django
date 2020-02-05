from django.urls import path
from usuario.views import UserListView

app_name = 'usuario'

urlpatterns = [
   path('usuario',UserListView.as_view(),name="lista"),
]