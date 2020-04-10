from django.urls import path
from user.views import RegisterView,LoginView, LogoutView, UserInfoView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('',UserInfoView.as_view(), name='user')
    ]