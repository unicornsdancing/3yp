from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
#from django.views.generic import direct_to_template
from energapp.models import *
from mysite.energapp import views

urlpatterns = patterns('',
    #url(r'^$',
    #    DetailView.as_view(
    #        model=Catz,
    #        template_name='energapp/index.html')),
    #url(r'^(?P<pk>\d+)/$',
    #    DetailView.as_view(
    #        model=Poll,
    #        template_name='polls/detail.html')),
    #url(r'^(?P<pk>\d+)/results/$',
    #    DetailView.as_view(
    #        model=Poll,
    #        template_name='polls/results.html'),
    #    name='polls_results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    #url(r'^(?P<poll_id>\d+)/addchoice/$','polls.views.add_choice'),
    url(r'^$', 'energapp.views.catz'),
    #url(r'^(?P<poll_id>\d+)/close/$', 'polls.views.closePoll')
)
