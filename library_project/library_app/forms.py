from django import forms
from .models import Book, Member, Issue

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['book', 'member', 'return_date']
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }
