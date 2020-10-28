from django.urls import path

from .views import NewUserView, UserView

urlpatterns = [
    path('user/', UserView.as_view()),
    path('user/create/', NewUserView.as_view()),
]
