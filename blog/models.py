from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):   #Модель создания поста
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    THEME = [
        ('Не открывается смена', 'Не открывается смена'),
        ('Не проводится продажа', 'Не проводится продажа'),
        ('Ошибка по кассе', 'Ошибка по кассе'),
        ('Нет доступа', 'Нет доступа'),
        ('Другое', 'Другое'),
    ]

    theme = models.CharField(
        max_length=200,
        choices=THEME,
        default='Другое',
        verbose_name="Категория заявки"
    )

    def is_upperclass(self):
        return self.theme

    text = models.TextField(verbose_name="Текст")
    published_date = models.DateTimeField(auto_now_add=True)

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
    date_comm = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


