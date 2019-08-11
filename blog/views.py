from django.utils import timezone
from .models import Post, Article
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import CommentForm
from django.core.paginator import Paginator
from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name = 'blog/base.html'

    def get_context_data(self, **kwargs):
        records = Article.objects.all()
        context = dict(records=records)
        return context

# Правило отображения постов
def post_list(request):
    posts_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts_list, 3)  # Колличество постов
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'post_list.html', {'posts': posts})


# Правило создание коммента
def comment_new(request, pk):
    if request.method == 'POST':  # Запрос метода == добавить данные
        form = CommentForm(request.POST)  # Cозданное форма (поля из шаблона)
        if form.is_valid():  # Проверяем валидацию формы(что бы поля совпадали для базы)
            comment = form.save(commit=False)  # Формо сохранил но не отправил
            comment.author_comm = request.user  # автор равен авторизированный пользователь
            comment.post_id = pk
            comment.save()  # сохранение коммента
    return redirect('post_detail', pk=pk)  # Переход на страницу (Детали просмотра, ID = комента к посту


# Правило отображения комментария к посту
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Article.objects.filter(post=pk).order_by('-date_comm')
    return render(request, 'post_detail.html', {'post': post, 'comments': comments})


# Правило нового поста
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


# Правило редактирование поста
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if post.author == request.user or request.user.is_superuser:
                post.published_date = timezone.now()
                post.save()
            else:
                return render(request, 'post_edit.html', {'form': form, "error": "Вы не являетесь автором"})
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'post_edit.html', {'form': form})


# Регистрацпия нового пользователя
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
