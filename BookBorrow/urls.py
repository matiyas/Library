from django.urls import path, re_path
from BookBorrow.views import CountryAutocomplete, LanguageAutocomplete, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    re_path(r'^country-autocomplete/$', CountryAutocomplete.as_view(), name='country-autocomplete'),
    re_path(r'^language-autocomplete/$', LanguageAutocomplete.as_view(), name='language-autocomplete'),
]
