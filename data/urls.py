from django.urls import path

from .views import DiaryListCreateView

urlpatterns = [
    path('diary/', DiaryListCreateView.as_view()),
    path('diary/<int:pk>', DiaryListCreateView.as_view()),
]
