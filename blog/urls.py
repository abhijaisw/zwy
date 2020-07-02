from django.urls import path
from . import views




urlpatterns = [
    path('', views.Blogindex, name="blogHome"),
    path('<int:id>/', views.Blogdetails, name="blog_detail"),
]
