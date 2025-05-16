from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_id = models.IntegerField(null=False)
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=200)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    location = models.CharField(max_length=200)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.first_name,self.last_name,self.phone)