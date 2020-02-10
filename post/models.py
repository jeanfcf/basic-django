from django.db import models
from usuario.models import User
# Create your models here.

class Post(models.Model):
    
    autor = models.ForeignKey(User, on_delete = models.CASCADE,verbose_name='autor',related_name='posts')
    conteudo = models.TextField(verbose_name='contDDDSeudo',default="",max_length=280)
    data = models.DateTimeField(verbose_name='Data',auto_now_add=True)
    imagem = models.ImageField(upload_to="posts/")
    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

    def __str__(self):
        return f'Autor: {self.autor} |  Data: {self.data} | ID: {self.id}'

    