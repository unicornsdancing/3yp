from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from energapp.models import *
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.urlresolvers import reverse
import datetime
import logging


@login_required
def profSettings(request, username):
    user = get_object_or_404(User, username=username)
    #create context
    #add user to context
    return render_to_response('settings.html/',context_instance=RequestContext(request))

@login_required
def uploadFreq(request, username):
    user= get_object_or_404(UserProfile, user__username=username) #get the UserProfile model object
    if request.method == 'GET': #if get
        return render_to_response('freq.html',{'user':user},context_instance=RequestContext(request)) #render the page with the form
    elif request.method == 'POST': #when done with the form
        c = request.POST.get('choice')
        try:
            if user.uploadFrequency != c: #if not the same
                user.uploadFrequency = c #then change
        except (KeyError, user.uploadFrequency == NULL):
            return render_to_response('freq.html', {
                'user': username,
                'error_message': "You didn't select new frequency.",
                }, context_instance=RequestContext(request))
        else:
            user.save() #save or leave the frequency
    return HttpResponseRedirect('/')

@login_required
def uploader(request, username):
    user = get_object_or_404(User, username=username)
    #create context
    #add user to context
    return render_to_response('uploader.html/',context_instance=RequestContext(request))

def generateSheet(request):
    return HttpResponse("generated sheet")

def pointsCalc(request):
    return HttpResponse("points: 9992")

@login_required
def pointsReset(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.get_profile()
    profile.points = 0
    profile.save()
    return render_to_response('index.html/',{'user':user},context_instance=RequestContext(request))

@login_required
def topsavers(request):
    return render_to_response('topsavers.html', {'range20': range(20)})

@login_required
def addAppliance(request, username):
    user= get_object_or_404(UserProfile, user__username=username) #get the UserProfile model object
    if request.method == 'GET': #if get
        return render_to_response('addAppliance.html',{'user':user},context_instance=RequestContext(request)) #render the page with the form
    elif request.method == 'POST': #when done with the form
        appliance = request.POST.get('newAppliance',None) #extract the appliance text box
        ucost = request.POST.get('userCost',None) #extract the cost text box
        if appliance == '': #if text box is empty, return error below
            return render_to_response('addAppliance.html',{'user':user,'error_message':'Please select a new appliance'},context_instance=RequestContext(request))

        user.appliance_set.add(Appliance(name=appliance,profile=user,cost=ucost)) #create a new appliance object and add to user's profile
        user.save() #save user
    return HttpResponseRedirect('/energapp/{}/settings/addAppliance'.format(user.user)) #return to the same page again

def about(request):
    return render_to_response("abojhut.html")