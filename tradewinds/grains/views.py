from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse
from .models import User, Firm, AccountType, Person, Account, Company

@login_required
def index(request):
    firms = Firm.objects.all().filter(owner=request.user)
    return render_to_response('grains/index.html',
           {'firms': firms, 'user': request.user}, RequestContext(request))

@login_required
def settings(request):
    account_types = AccountType.objects.all().filter(userId=request.user)
    return render_to_response('grains/account_settings.html',
           {'user': request.user, 'types': account_types}, RequestContext(request))


@login_required
def addFirm(request):
    firm_name = request.POST['firm']
    firm_already_exists = Firm.objects.all().filter(owner=request.user,name=firm_name)
    if firm_already_exists or firm_name == "":
    	return HttpResponseRedirect(reverse('grains:index'))
    firm = Firm(name=firm_name, owner=request.user)
    firm.save()
    return HttpResponseRedirect(reverse('grains:index'))

@login_required
def contacts(request):
    account_types = AccountType.objects.all().filter(userId=request.user)
    persons = Person.objects.all().filter(userId=request.user)
    companies = Company.objects.all().filter(userId=request.user)
    print companies[0]
    return render_to_response('grains/add_contact.html',
                             {'user': request.user, 'types': account_types, 'persons': persons, 'companies': companies}, RequestContext(request))    

@login_required
def viewFirm(request, firm_id):
    firm_exists = Firm.objects.all().filter(id=firm_id,owner=request.user)
    if firm_exists:
        account_types = AccountType.objects.all().filter(userId=request.user)
        #company_accounts = Account.objects.all().filter(firmId=firm_id)
        accounts = Account.objects.all().filter(firmId=firm_id)
    	persons = Person.objects.all().filter(userId=request.user)
        companies = Company.objects.all().filter(userId=request.user)
        return render_to_response('grains/firm.html',
           {'persons': persons, 'companies': companies, 'accounts': accounts , 'firm_id': firm_exists[0].id, 'user': request.user, 'types': account_types}, RequestContext(request))
    return HttpResponseRedirect(reverse('grains:index'))

@login_required
def addType(request):
    type_name = request.POST['typename']
    type_already_exists = AccountType.objects.all().filter(name=type_name, userId=request.user)
    if not type_already_exists  or type_name == "":
        accountType = AccountType(name=type_name, userId=request.user)
        accountType.save()
    return HttpResponseRedirect(reverse('grains:index'))

@login_required
def addPerson(request):
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']
    phone_num = request.POST['phonenum']
    website = request.POST['website']
    email = request.POST['email']
    person_exists = Person.objects.all().filter(phoneNum=phone_num,userId=request.user)
    if not person_exists:
        person = Person(firsName=first_name,lastName=last_name,phoneNum=phone_num,website=website,email=email,userId=request.user)
        person.save()
    return HttpResponseRedirect(reverse('grains:index'))    

@login_required
def addCompany(request):
    company_name = request.POST['companyname']
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']
    phone_num = request.POST['phonenum']
    website = request.POST['website']
    email = request.POST['email']
    company_exists = Company.objects.all().filter(name=company_name,userId=request.user)
    if not company_exists:
        person = Person(firsName=first_name,lastName=last_name,phoneNum=phone_num,website=website,email=email,userId=request.user)
        person.save()
        company = Company(name=company_name,phoneNum=phone_num,website=website,email=email,representative=person,userId=request.user)
        company.save()
    return HttpResponseRedirect(reverse('grains:index'))  


@login_required
def addAccount(request, firm_id):
    account_num = request.POST['accountnum']
    type_id = request.POST['accounttype']
    person_id = request.POST['person']
    company_id = request.POST['company']

    firm_exists = Firm.objects.all().filter(id=firm_id,owner=request.user)
    if firm_exists:
        account_type = AccountType.objects.get(id=type_id,userId=request.user)
        if person_id == "":
            company = Company(id=company_id,userId=request.user)
            account_exists = Account(firmId=firm_exists[0],company=company)
            if not account_exists:
                account = Account(firmId=firm_exists[0],accountType=account_type,accountNumber=account_num,company=company)
                account.save()
        else:    
            person = Person(id=person_id,userId=request.user)
            account_exists = Account(firmId=firm_exists[0],person=person)
            if not account_exists:
                account = Account(firmId=firm_exists[0],accountType=account_type,accountNumber=account_num,person=person)
                account.save()
        return HttpResponseRedirect(reverse('grains:viewFirm', args=[firm_id]))
    return HttpResponseRedirect(reverse('grains:index'))
