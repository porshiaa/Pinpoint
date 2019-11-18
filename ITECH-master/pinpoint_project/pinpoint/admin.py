from django.contrib import admin
from pinpoint.models import Destination
from pinpoint.models import UserProfile

# Register your models here.

admin.site.register(Destination)
admin.site.register(UserProfile)