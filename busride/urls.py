from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('book-ride/', views.dashboard, name='book_ride'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
      path('success/', views.success_view, name='success'),
  # URL for booking form submission
    path('logout/', auth_views.LogoutView.as_view(next_page='/busride/'), name='logout'),
    # Add more routes as needed
]
