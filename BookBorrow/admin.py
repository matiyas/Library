from django.contrib import admin
from .models import Reader, Book, Author
from .forms import ReaderForm, BookForm, AuthorForm


class ReaderAdmin(admin.ModelAdmin):
    form = ReaderForm


class BookAdmin(admin.ModelAdmin):
    form = BookForm


class BookInline(admin.StackedInline):
    model = Book
    form = BookForm
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    form = AuthorForm
    inlines = [BookInline, ]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Reader, ReaderAdmin)
admin.site.register(Book, BookAdmin)
