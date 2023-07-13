from django.contrib import admin

from .models import Exhibitor, MailCount


# Register your models here.

class ExhibitorAdmin(admin.ModelAdmin):
    # model = Exhibitor
    list_display = ['email', 'name', 'brand_name', 'BDEventID']
    search_fields = ['email', 'name', 'brand_name', 'BDEventID']


class CountAdmin(admin.ModelAdmin):
    # model = Exhibitor
    list_display = ['id', 'count']


admin.site.register(Exhibitor, ExhibitorAdmin)
admin.site.register(MailCount, CountAdmin)
