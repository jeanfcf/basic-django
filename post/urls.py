from django.urls import path
from post.views import PostListView,PostCreateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib import admin
from django.conf.urls import url
app_name = 'post'

urlpatterns = [
    path('posts',PostListView.as_view(),name="listaposts"),
    path('criarposts',PostCreateView.as_view(),name="criarpost"),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG == True:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, { 
            'document_root':settings.MEDIA_ROOT,
        }),
    ]