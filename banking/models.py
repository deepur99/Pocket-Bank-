from django.db import models

class Balance(models.Model):
    name=models.CharField(max_length=300)
    email=models.EmailField(max_length=300,unique=True,null=False)
    # email_id=models.EmailField(max_length=300,unique=True)
    # mobile_no=models.IntegerField()
    bank_id=models.CharField(max_length=300)
    # address=models.CharField(max_length=3000)
    balance=models.IntegerField()
    

    def __str__(self):
        return self.name


class After(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    sender = models.EmailField(max_length= 30)
    receiver = models.EmailField(max_length = 30)
    amt = models.IntegerField()

    def __str__(self):
        return self.sender

class Payments(models.Model):
    user = models.CharField(max_length = 100)
    amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user