from django.tasks import task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from.models import BorrowRecord
from datetime import date

@task
def send_overdue_reminder(user_id):
    user = User.objects.get(id=user_id)
    overdue = BorrowRecord.objects.filter(
        borrower=user, return_date__isnull=True, due_date__lt=date.today()
    )
    if overdue:
        book_list = "\n".join([f"- {r.book_instance.book.title}" for r in overdue])
        send_mail(
            subject="Library: Overdue Books Reminder",
            message=f"Hi {user.first_name},\n\nYou have overdue books:\n{book_list}\n\nPlease return them.",
            from_email="library@example.com",
            recipient_list=[user.email],
        )

@task
def send_welcome_email(user_email, username):
    send_mail(
        subject=f"Welcome to Library, {username}!",
        message="Your library account is active. You can borrow up to 3 books.",
        from_email="noreply@example.com",
        recipient_list=[user_email],
    )