from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gerenciador.views.home', name='home'),
    # url(r'^gerenciador/', include('gerenciador.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^$', 'agenda.views.index'),
    (r'^novo/$', 'agenda.views.novo'),
    (r'^exibir/(?P<num_item>\d+)/$', 'agenda.views.exibir'),
    (r'^remover/(?P<num_item>\d+)/$', 'agenda.views.remover'),
    
)
