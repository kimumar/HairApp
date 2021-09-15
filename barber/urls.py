from django.conf.urls import url
from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog-single/<int:pk>/', views.blogs, name='blog-single'),
    path('blog', views.blog, name='blog'),
    path('gallery', views.gallery, name='gallery'),
    path('services', views.services, name='services'),
    path('create', views.create, name='create'),
    path('blog-update/<str:pk>/', views.update, name='blog-update'),
    path('blog-delete/<int:pk>/', views.delete, name='blog-delete'),
    path('comment-update/<str:pk>/', views.updates, name='comment-update'),
    path('comment-delete/<int:pk>/', views.deleteco, name='comment-delete'),
]
