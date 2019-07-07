from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Hotel(models.Model):
    name = models.CharField(max_length=20)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=300, blank=True)
    born = models.DateField(null=True, blank=True)

# Форма комментария
class Article(models.Model):
    author_comm = models.ForeignKey(User, on_delete=models.CASCADE)
    body_comm = models.TextField()
    date_comm = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
