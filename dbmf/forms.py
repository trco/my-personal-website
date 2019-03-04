from django import forms

from .models import Book
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class BookForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['timestamp']
