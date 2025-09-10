from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest

from .models import Category, News, Comment
from .forms import CommentForm, NewsForm


def home(request: HttpRequest):
    newses = News.objects.all()
    categories = Category.objects.all()

    context = {
        "newses": newses,
        "categories": categories,
        "title": "Barcha maqolalar"
    }

    return render(request, "news/index.html", context)


def news_by_category(request, category_id: int):
    newses = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()

    context = {
        "newses": newses,
        "categories": categories,
        "title": Category.objects.get(pk=category_id).name
    }
    return render(request, "news/index.html", context)


def news_detail(request: HttpRequest, pk: int):
    categories = Category.objects.all()
    news = get_object_or_404(News, pk=pk)
    comments = Comment.objects.filter(news=news)

    news.views += 1
    news.save()

    context = {
        "news": news,
        "categories": categories,
        "title": news.title,
        'form': CommentForm(),
        'comments': comments,
    }
    return render(request, "news/news-detail.html", context)


def save_comment(request: HttpRequest, news_id: int):
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data["text"],
                news_id=news_id,
                user=request.user if request.user.is_authenticated else None
            )
    return redirect("news_detail", pk=news_id)


def save_news(request: HttpRequest):
    if request.method == "POST":
        form = NewsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            news = form.save()
            return redirect("news_detail", pk=news.pk)
    else:
        form = NewsForm()

    context = {
        "form": form,
        "title": "Yangi maqola qo‘shish"
    }

    return render(request, "news/add-news.html", context)


def update_news(request, pk: int):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(data=request.POST, files=request.FILES, instance=news)
        if form.is_valid():
            mews = form.save()
            return redirect("news_detail", pk=news.pk)
    else:
        form = NewsForm(instance=news)

    context = {
        "form": form,
    }

    return render(request, "news/add-news.html", context)


def delete_news(request, pk: int):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        news.delete()
        return redirect("home")
    else:
        context = {
            'title': news.title,
        }

        return render(request, "news/confirm-delete.html", context)