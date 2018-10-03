from dal import autocomplete
from django import forms
from BookBorrow.models import Country, Address


class AddressForm(forms.ModelForm):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=autocomplete.ModelSelect2(url='country-autocomplete')
    )

    class Meta:
        model = Address
        fields = ('__all__')

