# CRUD Operations on Book Model

## 1. Create
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984>
```

## 2. Retrieve
```python
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Output: ('1984', 'George Orwell', 1949)
```

## 3. Update
```python
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# Output: 'Nineteen Eighty-Four'
```

## 4. Delete
```python
book.delete()
Book.objects.all()
# Output: <QuerySet []>
```
