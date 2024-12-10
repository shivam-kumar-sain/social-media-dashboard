from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('analytics', views.analytics, name='analytics'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('password-reset/', views.password_reset, name='password_reset'),  
    path('create_social_media_platform/', views.create_social_media_platform, name='create_social_media_platform'),  
    path('social-media-profile/<int:id>', views.SocialMediaProfile, name='social-media-profile'),
]
