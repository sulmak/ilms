from django.contrib import admin
from .models import Author, Book, BookInstance, Category
# Register your models here.
admin.site.register(Author)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'category', 'available_copies')
    list_filter = ('author', 'category')
    search_fields = ('title', 'author__name', 'isbn')
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance)
admin.site.register(Category)
