from django.contrib import admin
from import_export.admin import ExportActionMixin

from .models import Details


# Register your models here.


# Register your models here.
class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('venue', 'city', 'country', 'BDEventID')


admin.site.register(Details, BookAdmin)
