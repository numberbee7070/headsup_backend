from django.urls import path

from .views import ListArticleView, RetrieveArticleView, ArticleFavouriteView

urlpatterns = [
    path('articles/', ListArticleView.as_view()),
    path('articles/<int:pk>', RetrieveArticleView.as_view()),
    path('favourite/<int:pk>', ArticleFavouriteView.as_view()),
]
