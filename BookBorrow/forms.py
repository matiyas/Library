from dal import autocomplete
from django import forms
from BookBorrow.models import Country, Language, Reader, Book, Author


def set_params(**dec_kwargs):
    class AutocompleteForm(forms.ModelForm):
        class Meta:
            model = dec_kwargs['model']
            fields = '__all__'

    setattr(AutocompleteForm, dec_kwargs['field'], forms.ModelChoiceField(
        queryset=dec_kwargs['autocomplete_model'].objects.all(),
        widget=autocomplete.ModelSelect2(url=dec_kwargs['url'])
    ))

    return AutocompleteForm


AuthorForm = set_params(field='country', autocomplete_model=Country, url='country-autocomplete', model=Author)


# class AuthorForm(forms.ModelForm):
#     country = forms.ModelChoiceField(
#         queryset=Country.objects.all(),
#         widget=autocomplete.ModelSelect2(url='country-autocomplete')
#     )
#
#     class Meta:
#         model = Author
#         fields = '__all__'


class ReaderForm(forms.ModelForm):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=autocomplete.ModelSelect2(url='country-autocomplete')
    )

    class Meta:
        model = Reader
        fields = '__all__'


class BookForm(forms.ModelForm):
    lang = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        widget=autocomplete.ModelSelect2(url='language-autocomplete')
    )

    class Meta:
        model = Book
        fields = '__all__'
