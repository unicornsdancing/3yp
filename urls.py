from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to, direct_to_template
from django.contrib import admin
from energapp import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('energapp.urls')),
    url(r'^auth/', include ('registration.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
