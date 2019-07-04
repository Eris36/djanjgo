from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('signup', views.signup, name='signup'),
    path('index', views.index, name='post_list'),
    path('comment',ListView.as_view( queryset=Reporter.objects.all().order_by( "-data" )[:20],
    template_name="templates/comment.html")),
]
