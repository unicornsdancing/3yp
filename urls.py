from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to, direct_to_template
from django.contrib import admin
from mysite.energapp import *
admin.autodiscover()
from mysite import settings

urlpatterns = patterns('',
    url(r'^$', redirect_to, {'url': '/energapp/'}),
    url(r'^energapp/', include('energapp.urls')),
    url(r'^auth/', include ('registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)