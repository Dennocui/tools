from django.contrib import admin
from django.db.models import Sum, Count, Q, F, Func
from django.db import models
# from django.forms import widgets


from import_export import resources, widgets
from import_export.fields import Field

from  . models import PrintingCost


class PrintingCostResource(resources.ModelResource):
    total_colored_cost= Field(column_name = 'Total Colored Cost',attribute='total_colored_cost')
    total_black_white_cost= Field(column_name = 'B&W Cost',attribute='total_black_white_cost')
    total_cost= Field(column_name = 'Total Cost',attribute='total_cost')
    variance = Field(column_name = 'Variance',attribute='variance')
    # margin = Field(column_name = 'Margin', attribute='margin', widget=widgets.FloatWidget())


    class Meta:
        model = PrintingCost
        fields = ('date','colored', 'black_white','black_white_cost','colored_cost','target_cost','total_colored_cost', 'total_black_white_cost', 'total_cost', 'variance',)
        export_order = ('date','colored', 'black_white','black_white_cost','colored_cost','target_cost','total_colored_cost', 'total_black_white_cost', 'total_cost', 'variance',)