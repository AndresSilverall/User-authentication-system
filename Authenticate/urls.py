from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('changepassword/', views.change_password, name="changepassword"),
    path('products/', views.products, name="products"),
]
