from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from bootstrap_modal_forms.generic import (
    BSModalLoginView,
    BSModalFormView,
    BSModalCreateView,
    BSModalUpdateView,
    BSModalReadView,
    BSModalDeleteView
)

from .forms import (
    BookModelForm,
    BookFilterForm
)
from .models import Book


class Dbmf(generic.ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'dbmf/dbmf.html'

    def get_queryset(self):
        qs = super().get_queryset()
        if 'type' in self.request.GET:
            qs = qs.filter(book_type=int(self.request.GET['type']))
        return qs


class BookFilterView(BSModalFormView):
    template_name = 'dbmf/filter_book.html'
    form_class = BookFilterForm

    def form_valid(self, form):
        self.filter = '?type=' + form.cleaned_data['type']
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('index') + self.filter


class BookCreateView(BSModalCreateView):
    template_name = 'dbmf/create_book.html'
    form_class = BookModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('dbmf:dbmf')


class BookUpdateView(BSModalUpdateView):
    model = Book
    template_name = 'dbmf/update_book.html'
    form_class = BookModelForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('dbmf:dbmf')


class BookReadView(BSModalReadView):
    model = Book
    template_name = 'dbmf/read_book.html'


class BookDeleteView(BSModalDeleteView):
    model = Book
    template_name = 'dbmf/delete_book.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('dbmf:dbmf')


def books(request):
    data = dict()
    if request.method == 'GET':
        books = Book.objects.all()
        data['table'] = render_to_string(
            'dbmf/_books_table.html',
            {'books': books},
            request=request
        )
        return JsonResponse(data)
