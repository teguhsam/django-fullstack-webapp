from app.models import Article
from django.shortcuts import render


def home(request):
    articles = Article.objects.all()
    return render(request, "app/home.html", {"articles": articles})
