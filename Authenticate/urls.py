from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('logged/', views.logged_user, name="logged"),
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('resetpassword/', views.reset_password, name="resetpassword"),
]
