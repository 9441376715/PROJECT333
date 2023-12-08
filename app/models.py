from django.db import models

# Create your models here.
class Capital(models.Model):
    capital_name=models.CharField(max_length=25,primary_key=True)
    def __str__(self):
        return self.capital_name

 
class Country(models.Model):
    country_name=models.CharField(max_length=50)
    capital_name=models.OneToOneField(Capital,on_delete=models.CASCADE)
    def __str__(self):
        return self.country_name
