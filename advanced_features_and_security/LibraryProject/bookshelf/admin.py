from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields shown in the list view
    list_display = ("title", "author", "publication_year")

    # Add filtering options on the right side of the admin
    list_filter = ("publication_year", "author")

    # Add a search box at the top
    search_fields = ("title", "author")
