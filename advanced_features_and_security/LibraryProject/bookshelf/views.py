from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        Book.objects.create(title=title, author=author, created_by=request.user)
        return redirect("book_list")
    return render(request, "bookshelf/book_form.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.save()
        return redirect("book_list")
    return render(request, "bookshelf/book_form.html", {"book": book})

@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})


from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Book
from .forms import BookForm

@csrf_protect
def book_list(request):
    query = request.GET.get("q")
    if query:
        # ✅ Safe: ORM prevents SQL injection
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@csrf_protect
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():  # ✅ Validate and sanitize input
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})
