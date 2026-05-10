from django.contrib import admin
from .models import BookLocation    
# Register your models here.
class BookLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'book', 'bin')
   
admin.site.register(BookLocation, BookLocationAdmin)