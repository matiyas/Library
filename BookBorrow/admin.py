from django.contrib import admin
from .models import Reader, Book, Author, Publishment
from .forms import ReaderForm, BookForm, AuthorForm


class BookInline(admin.StackedInline):
    model = Book
    form = BookForm
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    form = AuthorForm
    inlines = [BookInline, ]


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    form = ReaderForm


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    exclude = ('status', 'return_date')
    form = BookForm


@admin.register(Publishment)
class PublishmentAdmin(admin.ModelAdmin):
    model = Publishment

