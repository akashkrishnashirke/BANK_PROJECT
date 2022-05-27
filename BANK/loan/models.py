from django.db import models

# Create your models here.
class LoanApplicationModel(models.Model):
    name = models.CharField(max_length=30)
    income=models.IntegerField()
    mobileNo= models.BigIntegerField()
    address= models.CharField(max_length=50)