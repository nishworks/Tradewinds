from django.contrib import admin
from models import Account, AccountType, Person, Company, Firm, Transaction


admin.site.register(Account)
admin.site.register(AccountType)
admin.site.register(Person)
admin.site.register(Company)
admin.site.register(Firm)
admin.site.register(Transaction)
