from django.db import models

# Create your models here.


class Expense(models.Model):
    item = models.CharField(max_length=50)
    monthly_expense = models.IntegerField()

    def __str__(self) -> str:
        return self.item

    # @property
    # def added(self): 
    #     return 10
