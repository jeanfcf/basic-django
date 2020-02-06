from django.urls import path
from post.views import PostListView

app_name = 'post'

urlpatterns = [
    path('posts',PostListView.as_view(),name="lista"),
]