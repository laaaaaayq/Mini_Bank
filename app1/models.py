from django.db import models



# Create your models here.
class Register(models.Model):
    Acc_number=models.IntegerField(unique=True)
    Name=models.CharField(max_length=50)
    Amount=models.IntegerField()
    Phone=models.IntegerField()
    Password=models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Login(models.Model):
    Acc_number=models.IntegerField(unique=True)
    Password=models.CharField(max_length=50)

    # def __int__(self):
    #     return self.Acc_number