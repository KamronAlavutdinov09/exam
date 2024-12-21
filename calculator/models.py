from django.db import models

class Calculator(models.Model):
    infinity_number = models.FloatField()
    significant_digits = models.PositiveIntegerField()
    def __str__(self):
        return str(self.infinity_number)