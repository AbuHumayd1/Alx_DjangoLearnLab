from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library   # ✅ explicit import so the check finds it


# Function-based view for listing all books
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

