from statistics import variance
from turtle import colormode
from django.db import models

# Create your models here.

class PrintingCost(models.Model):
    date = models.DateField('Date')
    colored =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    black_white =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    colored_cost =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    black_white_cost  =  models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


    target_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.date


    def total_colored_cost(self):
        colored_cost_total = self.colored * self.colored_cost
        return colored_cost_total

    def total_black_white_cost(self):
        black_white_total = self.black_white * self.black_white_cost 
        return black_white_total

    def total_cost(self):
        total = self.total_black_white_cost() + self.total_colored_cost()
        return total
    
    def variance(self):
        variance =  self.target_cost - self.total_cost()
        return variance