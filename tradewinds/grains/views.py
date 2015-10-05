from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse
from .models import User, Firm

# Create your views here.
user = User.objects.get(username='nikhil')

class IndexView(generic.ListView):
    template_name = 'grains/home.html'
    context_object_name = 'firm_list'

    def get_queryset(self):
        """Return the firm names."""
        return Firm.objects.all().filter(owner=user)


def addFirm(request):
    firm_name = request.POST['firm']
    firm = Firm(name=firm_name, owner=user)
    firm.save()
    return HttpResponseRedirect(reverse('grains:index'))


