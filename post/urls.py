from django.urls import path
from post.views import PostListView,PostCreateView, PostDeleteView,PostUpdateView

app_name = 'post'

urlpatterns = [
    path('posts',PostListView.as_view(),name="listaposts"),
    path('criarposts',PostCreateView.as_view(),name="criarpost"),
    path('posts/<int:pk>/apagar',PostDeleteView.as_view(),name="deletarpost"),
    path('posts/<int:pk>/update',PostUpdateView.as_view(),name="updatepost")
]
