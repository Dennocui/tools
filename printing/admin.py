from importlib import resources
from django.contrib import admin

# Register your models here.


from . models import PrintingCost

from . resources import PrintingCostResource
from import_export.admin import ExportMixin 

@admin.register(PrintingCost)
class PrintingCostAdmin(ExportMixin,admin.ModelAdmin):
    resource_class= PrintingCostResource
    list_display = ('date','colored','black_white','colored_cost','black_white_cost','target_cost','total_colored_cost','total_black_white_cost','total_cost','variance')
    ordering =('-date',)