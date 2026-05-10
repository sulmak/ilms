from django.contrib import admin
from .models import Author, Book, BookInstance, Category
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    search_fields = ('name',)
admin.site.register(Author, AuthorAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'category', 'available_copies')
    list_filter = ('author', 'category')
    search_fields = ('title', 'author__name', 'isbn')
admin.site.register(Book, BookAdmin)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'imprint', 'due_back', 'status', 'borrower')
    list_filter = ('status', 'due_back')
    search_fields = ('book__title', 'imprint')
admin.site.register(BookInstance, BookInstanceAdmin )
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
admin.site.register(Category, CategoryAdmin)
