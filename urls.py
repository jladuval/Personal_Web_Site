from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin, auth
from django.http import HttpResponse

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^home/', 'home.views.index', name='Jacob Duval'),
    url(r'^(?i)resume', 'home.views.resume', name='Jacob Duval'),
    
    url(r'^(?i)SendEmail', 'home.views.SendEmail'),
    url(r'^', 'home.views.index', name='Jacob Duval'),

    #robots
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),
)
