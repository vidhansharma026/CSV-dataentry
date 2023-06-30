from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Data(models.Model):
    rollno = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(unique=True, validators=[RegexValidator("^[0-9]{10}$")])
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    fees = models.FloatField()

