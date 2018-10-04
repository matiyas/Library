from dal import autocomplete
from django import forms
from BookBorrow.models import Country, Reader


class ReaderForm(forms.ModelForm):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=autocomplete.ModelSelect2(url='country-autocomplete')
    )

    class Meta:
        model = Reader
        fields = ('__all__')


class 

