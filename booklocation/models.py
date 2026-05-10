from django.db import models

# Create your models here.

class BookLocation(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    book=models.ForeignKey('catalog.Book', on_delete=models.CASCADE, related_name='locations')
    bin=models.ForeignKey('bins.Bin', on_delete=models.SET_NULL, null=True, blank=True, related_name='book_locations')  

    def __str__(self): return self.name