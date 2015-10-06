from django.conf.urls import url

from views import form_example, addFirm, index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^addFirm$', addFirm, name='addFirm'),
    url(r'^settings$', form_example, name='layout'),
]
