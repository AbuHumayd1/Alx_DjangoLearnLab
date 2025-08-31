from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields shown in the list view
    list_display = ("title", "author", "publication_year")

    # Add filtering options on the right side of the admin
    list_filter = ("publication_year", "author")

    # Add a search box at the top
    search_fields = ("title", "author")

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add our custom fields to the admin forms
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# ✅ Register the CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)