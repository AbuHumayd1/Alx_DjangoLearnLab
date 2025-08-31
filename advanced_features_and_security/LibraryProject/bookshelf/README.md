# Permissions and Groups Setup

- Custom permissions are defined in `Book` model:
  - can_view, can_create, can_edit, can_delete
- Groups:
  - **Viewers**: can_view
  - **Editors**: can_view, can_create, can_edit
  - **Admins**: can_view, can_create, can_edit, can_delete
- Views are protected with `@permission_required`.
- Groups are automatically created via `post_migrate` signal in `bookshelf/signals.py`.
