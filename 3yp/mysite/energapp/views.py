from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from energapp.models import Catz
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.urlresolvers import reverse
import datetime
import logging

def catz(request):
    return render_to_response('index.html/',context_instance=RequestContext(request))