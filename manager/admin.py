from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib import admin
from .models import Book,Genre,Reviews


class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        skip_unchanged = True
        report_skipped = True
        import_id_fields= ('book_isbn',)
        fields = ('book_isbn', 'book_title', 'book_author', 'book_image', 'book_desc', 'book_genre_id') 

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('book_title','book_author')
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("genre_id","genre_name")
admin.site.register(Reviews)

 