from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name="Home"),
    path('about_us/', views.about, name="About"),
    path('about_me/', views.about_me, name="About_Me"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.log_out, name="logout")
]

