from django.http import HttpResponse
from dal import autocomplete
from .models import Country, Language


class AbstractAutocomplete(autocomplete.Select2QuerySetView):
    model = None
    objects_order = None

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return self.model.objects.none()

        qs = self.model.objects.all().order_by(self.objects_order)

        if self.q:
            qs = qs.filter(**{self.objects_order + '__istartswith': self.q}).order_by(self.objects_order)
        
        return qs


class CountryAutocomplete(AbstractAutocomplete):
    model = Country
    objects_order = 'english_name'


class LanguageAutocomplete(AbstractAutocomplete):
    model = Language
    objects_order = 'english_name'


def index(request):
    return HttpResponse('<h1>Hello World!</h1>')
