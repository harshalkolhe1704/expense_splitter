from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def form_valid(self, form):
        messages.success(self.request, 'Login successful!')
        return super().form_valid(form)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Assign the current user
            expense.save()
            return redirect('history')
    else:
        form = ExpenseForm()
    return render(request, 'splitter/add_expense.html', {'form': form})

@login_required
def expense_history(request):
    # Filter expenses by the current user
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'splitter/history.html', {'expenses': expenses})
