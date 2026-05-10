from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, timedelta
from bins.models import Bin 

class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self): return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)    
    summary = models.TextField()
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    published_date = models.DateField()
    total_copies = models.PositiveIntegerField(default=1)
    bin = models.ForeignKey(Bin, on_delete=models.SET_NULL, null=True, blank=True, related_name='books')
    

    def available_copies(self):
        return self.total_copies - self.bookinstance_set.filter(status='o').count()

    def get_absolute_url(self):
        return reverse('catalog:book-detail', args=[self.id])

    def __str__(self): return self.title

class BookInstance(models.Model):
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=200, help_text="Edition, publisher, year")
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='a')

    class Meta:
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return f'{self.id} ({self.book.title})'
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self): return self.name
    def get_absolute_url(self): return reverse('author-detail', args=[str(self.id)])

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta: verbose_name_plural = "Categories"
    def __str__(self): return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character ISBN')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000)
    cover = models.ImageField(upload_to='covers/', blank=True)
    published_date = models.DateField()
    total_copies = models.PositiveIntegerField(default=1)

    def available_copies(self):
        return self.total_copies - self.bookinstance_set.filter(status='o').count()

    def __str__(self): return self.title
    def get_absolute_url(self): return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='a')

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self): return f'{self.id} ({self.book.title})'

    @property
    def is_overdue(self):
        return bool(self.due_back and date.today() > self.due_back)