from django.conf.urls import url

from views import contacts, addFirm, index, viewFirm, addType, addAccount
from views import addPerson, addCompany, settings

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^addFirm$', addFirm, name='addFirm'),
    url(r'^contacts$', contacts, name='contacts'),
    url(r'^settings$', settings, name='settings'),
    url(r'^(?P<firm_id>[0-9]+)/$', viewFirm, name='viewFirm'),
    url(r'^addType$', addType, name='addType'),
    url(r'^addPerson$', addPerson, name='addPerson'),
    url(r'^addCompany$', addCompany, name='addCompany'),
    url(r'^addAccount/(?P<firm_id>[0-9]+)/$', addAccount, name='addAccount'),
]
