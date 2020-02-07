from django.db import models
from usuario.models import User
# Create your models here.

class Post(models.Model):
    
    autor = models.ForeignKey(User, on_delete = models.CASCADE,verbose_name='autor')
    conteudo = models.TextField(verbose_name='contDDDSeudo',default="",max_length=280)
    data = models.DateTimeField(verbose_name='Data',auto_now_add=True)
    imagem = models.ImageField(default="posts/Tapioca_rendada.jpg",upload_to="posts/",blank=True,null=True);

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

    def __str__(self):
        return f'Autor: {self.autor} |  Data: {self.data}'

    