from django.urls import path

from .views import DiaryListCreateView, ListArticleView, RetrieveArticleView

urlpatterns = [
    path('diary/', DiaryListCreateView.as_view()),
    path('articles/', ListArticleView.as_view()),
    path('articles/<int:pk>', RetrieveArticleView.as_view()),
]
