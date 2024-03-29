from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/create/', views.BookCreate.as_view(),
         name='book_create'),
    path('book/update/<int:pk>', views.BookUpdate.as_view(),
         name='book_update'),
    path('book/delete/<int:pk>', views.BookDelete.as_view(),
         name='book_delete'),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('edit/<int:author_id>/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('delete/<int:author_id>', views.delete, name='delete'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(),
         name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('my_books/', views.LoanedBookByUserListView.as_view(), name='my-borrowed'),
]
