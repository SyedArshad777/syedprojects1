from django.urls import path
from . import views

urlpatterns = [
    path('add-book/', views.add_book, name='add_book'),
    path('books/', views.book_list, name='book_list'),
    path('add-member/', views.add_member, name='add_member'),
    path('members/', views.member_list, name='member_list'),
    path('issue-book/', views.issue_book, name='issue_book'),
    path('issues/', views.issue_list, name='issue_list'),
]