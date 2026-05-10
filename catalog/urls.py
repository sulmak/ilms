from django.urls import path
from. import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('dashboard/', views.async_dashboard, name='dashboard'),
]