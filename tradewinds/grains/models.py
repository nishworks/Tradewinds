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
    userId = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.firsName + " " + self.lastName) 


class Company(models.Model):

    name = models.CharField(max_length=150)
    representative = models.ForeignKey(Person)
    phoneNum = models.CharField(max_length=15)
    website = models.URLField()
    email = models.EmailField()
    userId = models.ForeignKey(User)

    def __unicode__(self):
        return self.name
        

class Firm(models.Model):

    name = models.CharField(max_length=150)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name


class AccountType(models.Model):

    userId = models.ForeignKey(User)
    name = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Account(models.Model):

    firmId = models.ForeignKey(Firm)
    accountType = models.ForeignKey(AccountType)
    accountNumber = models.CharField(max_length=15)
    person = models.ForeignKey(Person, null=True)
    company = models.ForeignKey(Company, null=True)

    def __unicode__(self):
        return self.accountNumber


class TransactionType(models.Model):

    name = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    
    def __unicode__(self):
        return self.name


class Transaction(models.Model):

    firmId = models.CharField(max_length=150)
    account = models.ForeignKey(Account)
    amount = models.IntegerField()
    description = models.CharField(max_length=150)
    txType = models.ForeignKey(TransactionType)
