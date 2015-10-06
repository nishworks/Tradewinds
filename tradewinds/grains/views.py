from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse
from .models import User, Firm

@login_required
def index(request):
    firms = Firm.objects.all().filter(owner=request.user)
    return render_to_response('grains/index.html',
           {'firms': firms, 'user': request.user}, RequestContext(request))

@login_required
def addFirm(request):
    firm_name = request.POST['firm']
    firm = Firm(name=firm_name, owner=request.user)
    firm.save()
    return HttpResponseRedirect(reverse('grains:index'))

@login_required
def form_example(request):
    return render_to_response('grains/form_example.html',
                             {'user': request.user}, RequestContext(request))
