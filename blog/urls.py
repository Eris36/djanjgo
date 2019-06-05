from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
<<<<<<< HEAD
    path('register', views.register, name='register'),
    path('index', views.index, name='index'),
=======
>>>>>>> c38ab55dba45b82747b6b1bb4ab44b6780e3352f
    
]