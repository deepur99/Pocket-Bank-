from django.db import models

class Balance(models.Model):
    name=models.CharField(max_length=300)
    bank_id=models.IntegerField(unique=True,null=False)
    balance=models.IntegerField()
    email=models.EmailField(max_length=300,unique=True)

    def __str__(self):
        return self.name


class After(models.Model):
    date = models.DateTimeField(auto_now_add = True)
    sender = models.EmailField(max_length= 30)
    receiver = models.EmailField(max_length = 30)
    amt = models.IntegerField()

    def __str__(self):
        return self.sender
