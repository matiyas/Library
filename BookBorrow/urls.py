from django.urls import path, re_path
from . import views
from BookBorrow.views import CountryAutocomplete


urlpatterns = [
    path('', views.Index),
    re_path(r'^country-autocomplete/$', CountryAutocomplete.as_view(), name='country-autocomplete'),
]
