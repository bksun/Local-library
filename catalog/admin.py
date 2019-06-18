from catalog.models import Author, Genre, Book, BookInstance, Language, AuthorAdmin, BookAdmin, BookAdmin,BookInstanceAdmin
from django.contrib import admin

# Register your models here.


# Register the admin class with the associated model
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(Language)
