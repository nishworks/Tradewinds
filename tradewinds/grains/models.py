from django.db import models
from django.contrib.auth.models import User

__doc__ ="""

    NOTES
        * By default, for every model, django creates
            id = models.AutoField(primary_key=True)

    TODO
        * datetime - We will add time related data fields shortly.
        *

"""

# Create your models here.
class Person(models.Model):

    firsName = models.CharField(max_length=60)
    lastName = models.CharField(max_length=60)
    phoneNum = models.CharField(max_length=15)
    website = models.URLField()
    email = models.EmailField()


class Company(models.Model):

    name = models.CharField(max_length=150)
    representative = models.ForeignKey(Person)
    phoneNum = models.CharField(max_length=15)
    website = models.URLField()
    email = models.EmailField()


class Firm(models.Model):

    name = models.CharField(max_length=150)
    owner = models.ForeignKey(User)


class AccountType(models.Model):

    firmId = models.ForeignKey(Firm)
    name = models.CharField(max_length=15)


class Account(models.Model):

    firmId = models.ForeignKey(Firm)
    accountType = models.ForeignKey(AccountType)
    accountNumber = models.CharField(max_length=15)
    owner = models.ForeignKey(Person, null=True)
    owner = models.ForeignKey(Company, null=True)


class TransactionType(models.Model):

    name = models.CharField(max_length=15)
    description = models.CharField(max_length=150)


class Transaction(models.Model):

    firmId = models.CharField(max_length=150)
    account = models.ForeignKey(Account)
    amount = models.IntegerField()
    description = models.CharField(max_length=150)
    txType = models.ForeignKey(TransactionType)
