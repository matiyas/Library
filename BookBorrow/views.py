from django.shortcuts import render
from django.http import HttpResponse
from dal import autocomplete
from BookBorrow.models import Country


class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Country.objects.none()

        qs = Country.objects.all().order_by('english_name')

        if self.q:
            qs = qs.filter(english_name__istartswith=self.q).order_by('english_name')
        
        return qs


def Index(request):
    return HttpResponse('<h1>Hello World!</h1>')
