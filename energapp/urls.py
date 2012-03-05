from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
#from django.views.generic import direct_to_template
from energapp.models import *
from energapp import views
from django.views.generic.simple import redirect_to, direct_to_template
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Appliance.objects.order_by('-name'),
            context_object_name='appliances',
            template_name='index.html')), #home page list
    #url(r'^$', 'energapp.views.index', name="index"),
    url(r'^(?P<username>\w+)/settings/$', 'energapp.views.profSettings', name="user-settings"), #settings page
    url(r'^(?P<username>\w+)/settings/pointsReset/$', 'energapp.views.pointsReset', name="user-reset"), #points reset page
    url(r'^(?P<username>\w+)/settings/addAppliance/$', 'energapp.views.addAppliance', name="user-appliances"),#add new appliance page
    url(r'^(?P<username>\w+)/settings/uploadFrequency/$', 'energapp.views.uploadFreq', name="user-freq"),#upload frequency men
    url(r'^(?P<username>\w+)/upload/$', 'energapp.views.uploadFunc', name="user-uploader"), #uploader of the data
    url(r'^about/$',
        TemplateView.as_view(
            template_name="about.html"),
        name="about"),
    url(r'^topsavers/$',
        ListView.as_view(
            queryset=UserProfile.objects.order_by('-points'),
            context_object_name='savers_list',
            template_name='topsavers.html'),
        name="user-top"), #top savers list
)
