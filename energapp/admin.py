from django.contrib import admin
from energapp.models import *

class ApplianceInline(admin.TabularInline):
    model = Appliance
    extra = 3
class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,			{'fields': ['user', 'points', 'consumption', 'uploadFrequency']}),
    ]
    inlines = [ApplianceInline]

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Appliance)