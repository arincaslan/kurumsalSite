from django.shortcuts import render,redirect
from .models import Article
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def articles(request):
    articles = Article.objects.all()
    paginator = Paginator(articles,6)
    page = request.GET.get('page')
    makale = paginator.get_page(page)
    return render(request, "articles.html", {'makale' : makale})


def article_detail(request, articleslug):
    article = Article.objects.get(article_slug=articleslug)
    return render(request, "article_detail.html",{'nbar' : 'article_detail','article': article})
