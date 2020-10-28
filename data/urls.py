from django.urls import path

from .views import DiaryListCreateView, article_view

urlpatterns = [
    path('diary/', DiaryListCreateView.as_view()),
    path('articles/', article_view),
    path('articles/<int:chapter>', article_view),
]
