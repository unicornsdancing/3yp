import datetime
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User, UserManager

UPLOAD_CHOICES = (
    ('weekly', 'Week'),
    ('daily', 'Day'),
    ('monthly', 'Month')
)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    points = models.IntegerField(default=0) #points calculated (overall: both app + server)
    #friend = models.ManyToManyField(User) #friends assoced
    uploadFrequency = models.CharField(max_length=10, choices=UPLOAD_CHOICES) #how often to upload
    consumption = models.IntegerField(default=0) #how much has a user used energy
    #up_date = models.DateTimeField('upload date') #time of the last upload

    def __unicode__(self):
        return unicode(self.user)
    #def up_date_today(self):
    #    return self.up_date.date() == datetime.date.today()
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

class Appliance(models.Model):
    name = models.CharField(max_length=200) #what is it
    profile = models.ForeignKey(UserProfile) #who uses them
    cost = models.IntegerField() #how expensive is it per kw

    def __unicode__(self):
        return self.name