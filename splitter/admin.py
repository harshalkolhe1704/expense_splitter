from django.contrib import admin
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'user', 'date')
    list_filter = ('user', 'date')
    search_fields = ('title', 'participants')
