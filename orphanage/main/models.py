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
    

class Celebrate_Together(models.Model):
    first_name = models.CharField(max_length=30,null = True)
    last_name = models.CharField(max_length=30,null = True)
    phone_number = models.CharField(max_length=10,null = True)
    reason=models.CharField(max_length=30,null = True)
    email = models.EmailField(default='',null = True)
    date_field=models.DateField(null=True)

class Contact_info(models.Model):
    name = models.CharField(max_length = 200)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    subject=models.CharField(max_length=30)
    Message=models.CharField(max_length=1000)


