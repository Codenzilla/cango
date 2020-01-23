from django.contrib import admin
from django.urls import path

from . import views
app_name = "makale"

urlpatterns = [
    path('dashboard/', views.dashboard, name = "dashboard"),
    path('makaleekle/', views.makaleekle, name = "makaleekle"),
    path('makale/<int:id>', views.detail, name = "detail"),
    path('update/<int:id>', views.updateArticle, name = "update"),
    path('delete/<int:id>', views.deleteArticle, name = "delete"),
    path('', views.makale, name = "makale"),
    path('comment/<int:id>', views.addComment, name = "comment"),
]