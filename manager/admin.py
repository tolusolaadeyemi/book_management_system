from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Book,Genre,Reviews


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('book_title','book_author')
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("genre_id","genre_name")
admin.site.register(Reviews)
admin.site.register(BookAdmin)
 