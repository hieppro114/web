from django.db import models
# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    number_of_page = models.DecimalField(max_digits=15, decimal_places=10)
    description = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_date = models.CharField(max_length=100)

    class Meta:
        db_table = "tblemployee"
