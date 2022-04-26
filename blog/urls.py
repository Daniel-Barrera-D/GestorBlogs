from django.urls import path

#Views
from . import views

#Config URL
urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:id>/', views.blog, name='blogs'),
]