from django.shortcuts import render, redirect
from .forms import BookForm, MemberForm, IssueForm
from .models import Book, Member, Issue

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library_app/add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library_app/book_list.html', {'books': books})

def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'library_app/add_member.html', {'form': form})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'library_app/member_list.html', {'members': members})

def issue_book(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.book.available_copies -= 1
            issue.book.save()
            issue.save()
            return redirect('issue_list')
    else:
        form = IssueForm()
    return render(request, 'library_app/issue_book.html', {'form': form})

def issue_list(request):
    issues = Issue.objects.all()
    return render(request, 'library_app/issue_list.html', {'issues': issues})
