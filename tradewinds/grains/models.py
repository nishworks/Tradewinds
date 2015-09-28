from django.db import models


# Create your models here.
class Person(models.Model):

    # By default from django - id = models.AutoField(primary_key=True)
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
