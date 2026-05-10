from django.db import models
from django.contrib.auth.models import User
from catalog.models import BookInstance
from decimal import Decimal
from datetime import date, timedelta

class Member(models.Model):
    MEMBERSHIP_CHOICES = [('S', 'Student'), ('F', 'Faculty'), ('P', 'Public')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default='P')
    phone = models.CharField(max_length=15, blank=True)
    max_books = models.PositiveIntegerField(default=3)

    def __str__(self): return self.user.username

class BorrowRecord(models.Model):
    book_instance = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    late_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = date.today() + timedelta(days=14)
        super().save(*args, **kwargs)

    @property
    def is_overdue(self):
        if self.return_date: return False
        return date.today() > self.due_date

    def calculate_fee(self):
        if self.is_overdue:
            days_late = (date.today() - self.due_date).days
            self.late_fee = Decimal(days_late) * Decimal('0.50') # $0.50/day
        return self.late_fee
class MemberProfile(models.Model):
    MEMBERSHIP = [('S', 'Student'), ('F', 'Faculty'), ('P', 'Public')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=1, choices=MEMBERSHIP, default='P')
    phone = models.CharField(max_length=15, blank=True)
    max_books = models.PositiveIntegerField(default=3)

class BorrowRecord(models.Model):
    book_instance = models.ForeignKey(BookInstance, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    late_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = date.today() + timedelta(days=14)
        super().save(*args, **kwargs)

    def calculate_fee(self):
        if self.return_date and self.return_date > self.due_date:
            days_late = (self.return_date - self.due_date).days
            self.late_fee = Decimal(days_late) * Decimal('0.50')
        elif not self.return_date and date.today() > self.due_date:
            days_late = (date.today() - self.due_date).days
            self.late_fee = Decimal(days_late) * Decimal('0.50')
        return self.late_fee