from django.db import models

from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

from oauth2client.contrib.django_util.models import CredentialsField

from django.conf import settings



# Create your models here.

class CredentialsModel(models.Model):

    id = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, related_name='credentials')

    credential = CredentialsField()

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

class Destination(models.Model):

    name = models.CharField(max_length=50)

    location = models.CharField(max_length=50, default='none')

    description = models.TextField(default=0)

    image = models.ImageField(upload_to='island_images', default="none")

    #image = models.CharField(max_length=100, default='no image')

    long = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    lat = models.DecimalField(max_digits=9, decimal_places=6, default=0)

    climate = models.CharField(max_length=25, default='none')

    budget = models.CharField(max_length=10, default='none')

    activities = models.TextField(default="none")

    weather = models.CharField(max_length=300,default="none");

    slug = models.SlugField(unique=True, default='none')



    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)



        super(Destination, self).save(*args, **kwargs)



    def __str__(self):

        return self.name







class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.

    user = models.OneToOneField(User)

    # The additional attributes we wish to include

    picture = models.ImageField(upload_to='profile_images')







    # Override the __unicode__() method to return out something meaningful!



    def __str__(self):

        return self.user.username

        
