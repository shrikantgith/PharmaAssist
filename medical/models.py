from django.db import models

# Create your models here.


class Medicine(models.Model):
    name= models.CharField(max_length=100)
    quantity=models.IntegerField()
    purchase_date=models.DateTimeField()
    expiration_date=models.DateTimeField()
#   auto_reco=models.BooleanField()
    def __str__(self):
        return self.name

class Patient(models.Model):
#    auto_reco= models.BooleanField()
    Patient_Name=models.CharField(max_length=100)
    Address= models.CharField(max_length=100)
    City= models.CharField(max_length=100)
    Doctor= models.CharField(max_length=50)
    Phno_NO= models.BigIntegerField()
    medicine = models.ManyToManyField(Medicine)
    def __str__(self):

        return self.Patient_Name
