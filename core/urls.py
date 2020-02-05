from django.urls import path
from core.views import index,contatos

app_name = 'core'

urlpatterns = [
    path('', index,name='index'),
    path('contatos',contatos,name='contatos'),
]