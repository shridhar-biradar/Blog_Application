from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('create/', views.create_blog_view, name='create_blog'),
    path('detail/<int:id>/', views.blog_detail_view, name='blog_detail'),
    path('blog/edit/<int:id>/', views.edit_blog, name='edit_blog'),
    path('blog/delete/<int:id>/', views.delete_blog, name='delete_blog'),
    
    path('api/signup/', views.register_user, name='api_signup'),
    path('api/login/', views.api_login_user, name='api_login'),
    path('api/logout/', views.logout_user, name='api_logout'),
    path('api/create/', views.create_blog, name='api_create_blog'),
]
