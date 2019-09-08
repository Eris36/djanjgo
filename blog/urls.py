from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('signup', views.signup, name='signup'),
    path('comment/<int:pk>/', views.comment_new, name='comment_new'),
    path('test_post', views.test_post, name='test_post'),
    path('post_delete/<int:pk>/', views.post_delete, name="post_delete"),

]
