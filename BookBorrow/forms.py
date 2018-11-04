from dal import autocomplete
from django import forms
from BookBorrow.models import Country, Reader, Book, Author, Language


def autocomplete_form_class(**kwargs):
    class AutocompleteForm(forms.ModelForm):
        locals()[kwargs['field']] = forms.ModelChoiceField(
            queryset=kwargs['autocomplete_model'].objects.all(),
            widget=autocomplete.ModelSelect2(url=kwargs['url'])
        )

        class Meta:
            model = kwargs['model']
            fields = '__all__'

    return AutocompleteForm


ReaderForm = autocomplete_form_class(
    field='country',
    autocomplete_model=Country,
    url='country-autocomplete',
    model=Reader
)
BookForm = autocomplete_form_class(
    field='lang',
    autocomplete_model=Language,
    url='language-autocomplete',
    model=Book
)
