from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'participants']
        widgets = {
            'participants': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter names separated by commas (e.g. Alice, Bob, Charlie)'}),
        }
