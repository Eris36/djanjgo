from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Это поле обязательно')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

#Форма для комментария
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)


class Сomment(models.Model):
    post = Posts(r = Reporter(first_name='John', last_name='Smith', email='john@example.com'))
    post.save()

