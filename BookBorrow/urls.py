from django.urls import path, re_path
from . import views
from BookBorrow.views import CountryAutocomplete, LanguageAutocomplete


urlpatterns = [
    path('', views.index),
    re_path(r'^country-autocomplete/$', CountryAutocomplete.as_view(), name='country-autocomplete'),
    re_path(r'^language-autocomplete/$', LanguageAutocomplete.as_view(), name='language-autocomplete'),
]
