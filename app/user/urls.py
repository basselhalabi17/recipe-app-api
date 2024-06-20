"""
URL mappings for user API
"""

from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='create'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('profile/', views.ManageUserView.as_view(), name='profile'),
]
