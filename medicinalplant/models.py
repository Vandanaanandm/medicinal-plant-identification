from django.db import models



class regtable(models.Model):
    name=models.CharField(max_length=150)
    address=models.CharField(max_length=150)
    phone=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    password=models.CharField(max_length=150)


class fileuploadtable(models.Model):
    image=models.FileField(max_length=150)
    name=models.CharField(max_length=150)