from django.contrib import admin
from shelf.models import Book, Group

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'writer', 'publisher', 'group', 'amount']
    search_fields = ['title', 'writer','publisher']
    list_filter = ('group',)
    list_per_page = 2 

admin.site.register(Book, BookAdmin)
admin.site.register(Group)
