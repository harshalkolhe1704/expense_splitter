from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from splitter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_expense, name='add'),
    path('history/', views.expense_history, name='history'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
