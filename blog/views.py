from gc import get_objects
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from blog.forms import CommentForm
from blog.models import Article, Comment


def home(request):
        article = Article.objects.all()
        context = {
            'articles': article
        }
        return render(request, 'home.html', context)


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def labSix(request):
    return render(request, "LAB6.html")

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)  # Получаем статью или 404 ошибку
    if request.method == "POST":
        form = CommentForm(request.POST)  # Получаем данные из формы
        if form.is_valid():  # Проверяем валидность формы
            if request.user.is_authenticated:  # Проверяем авторизацию пользователя
                comment = Comment(
                    article=article,
                    user=request.user,  # Используем имя авторизованного пользователя
                    comment=form.cleaned_data["comment"]
                )
                try:
                    comment.save()  # Сохраняем комментарий в базе данных
                    return redirect('article', article_id)  # Обновляем страницу со статьей
                except Exception as Ex:
                    print(Ex)
                    form.add_error(None, 'Ошибка добавления комментария')
            else:
                return redirect("login")
    else:
        form = CommentForm()
    return render(request, 'article.html', {
        'article': article,
        'comment': article.comment_set.all(),
        'form': form
    })


