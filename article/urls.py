from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "article"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name=index),
]
