from django.urls import path

from .views import NewUserView, UserInfoView

urlpatterns = [
    path('user/', UserInfoView.as_view()),
    path('user/create/', NewUserView.as_view()),
]
