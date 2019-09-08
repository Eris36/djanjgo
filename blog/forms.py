from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Article


class PostForm(forms.ModelForm): #Формы статей
    class Meta:
        model = Post
        fields = ('title', 'theme', 'text',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')

    class Meta:     #Формы регистрации пользователя
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class CommentForm(forms.ModelForm):  #Форма комментария
    class Meta:
        model = Article
        fields = ('body_comm',)

