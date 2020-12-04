from django.urls import path

from .views import NewUserView, UserInfoView, UserRenameView

urlpatterns = [
    path('user/', UserInfoView.as_view()),
    path('user/rename/', UserRenameView.as_view()),
    path('user/create/', NewUserView.as_view()),
]
