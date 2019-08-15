from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "article"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('articles/', views.articles, name = "articles"),
    path('article/<slug:article_slug>', views.article_detail, name="articleDetail")
]
