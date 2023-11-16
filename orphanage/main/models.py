from django.db import models


class Donate_Money(models.Model):

    first_name = models.CharField(max_length=30,null = True)
    last_name = models.CharField(max_length=30,null = True)
    phone_number = models.CharField(max_length=10,null = True)
    comment = models.CharField(max_length=100,null = True)
    email = models.EmailField(default='',null = True)
    amount = models.IntegerField(default=0,null = True)

class Volunteer_Work(models.Model):
    first_name = models.CharField(max_length=30,null = True)
    last_name = models.CharField(max_length=30,null = True)
    phone_number = models.CharField(max_length=10,null = True)
    volun=models.CharField(max_length=30,null = True)
    available = models.CharField(max_length=3, choices=(('yes', 'Yes'), ('no', 'No')), default='yes')

    def __str__(self):
        return f"{self.volun}"