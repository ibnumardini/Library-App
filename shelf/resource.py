from import_export import resources
from shelf.models import Book
from import_export.fields import Field


class BookResource(resources.ModelResource):
    
    group__name = Field(attribute='group', column_name="group")
    
    class Meta:
        model = Book
        fields = ['title', 'writer', 'publisher', 'amount', 'group__name']
        export_order = ['title', 'writer', 'publisher', 'amount', 'group__name']
