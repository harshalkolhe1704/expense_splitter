from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('history')
    else:
        form = ExpenseForm()
    return render(request, 'splitter/add_expense.html', {'form': form})

def expense_history(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'splitter/history.html', {'expenses': expenses})
