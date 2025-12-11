from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_expense, name='add_expense'),
    path('history/', views.expense_history, name='history'),
]
