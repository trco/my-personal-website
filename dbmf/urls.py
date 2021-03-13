from django.urls import path

from dbmf import views


app_name = 'dbmf'
urlpatterns = [
    path('', views.Dbmf.as_view(), name='dbmf'),
    path('books/', views.books, name='books'),
    path('filter/', views.BookFilterView.as_view(), name='filter_book'),
    path('create/', views.BookCreateView.as_view(), name='create_book'),
    path('update/<int:pk>', views.BookUpdateView.as_view(), name='update_book'),
    path('read/<int:pk>', views.BookReadView.as_view(), name='read_book'),
    path('delete/<int:pk>', views.BookDeleteView.as_view(), name='delete_book')
]
