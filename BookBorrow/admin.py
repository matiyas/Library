from django.contrib import admin
from .models import Reader, Book, Address
from .forms import AddressForm


class ReaderInline(admin.StackedInline):
    model = Reader


class AddressAdmin(admin.ModelAdmin):
    form = AddressForm
    inlines = (ReaderInline,)


admin.site.register(Address, AddressAdmin)
# admin.site.register(Reader, ReaderAdmin)
