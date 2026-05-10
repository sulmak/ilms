from django.http import HttpResponse
from django.template import loader
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from.models import Book, Author, BookInstance
from circulation.models import BorrowRecord
from datetime import date, timedelta
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q, Count

class BookListView(generic.ListView):
    model = Book
    paginate_by = 12
    template_name = 'catalog/book_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) |
                Q(author__name__icontains=query) |
                Q(isbn__icontains=query)
            )
        return Book.objects.all()

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BorrowRecord
    template_name = 'catalog/bookinstance_list_borrowed_user.html'

    def get_queryset(self):
        return BorrowRecord.objects.filter(
            borrower=self.request.user
        )

class LoanedBooksAllListView(PermissionRequiredMixin, generic.ListView):
    model = BorrowRecord
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_all.html'

    def get_queryset(self):
        return BorrowRecord.objects.filter(
            book_instance__status='o'
        ).order_by('due_date')
async def async_dashboard(request):
    # Django 6: AsyncPaginator【1236953943921658097】
    from django.core.paginator import AsyncPaginator
    books = Book.objects.annotate(num_loans=Count('bookinstance__borrowrecord'))
    paginator = AsyncPaginator(books.order_by('-num_loans'), 5)
    page = await paginator.aget_page(request.GET.get('page', 1))
    return render(request, 'catalog/dashboard.html', {'page': page})