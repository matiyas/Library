from django.contrib import admin
from .models import Reader, Book
from .forms import ReaderForm


class ReaderAdmin(admin.ModelAdmin):
    form = ReaderForm


admin.site.register(Reader, ReaderAdmin)
admin.site.register(Book)
