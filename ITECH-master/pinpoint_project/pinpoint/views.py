from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from pinpoint.models import Destination
from pinpoint.forms import UserForm, UserProfileForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.forms import UserChangeForm


from django.views import View

from django.contrib.auth.models import User

import httplib2

from django.contrib.auth import login

#requirements for Google oauth2client

from oauth2client.contrib.django_util.storage import DjangoORMStorage

from apiclient import discovery

from oauth2client import client, tools

from oauth2client.file import Storage

from oauth2client.client import OAuth2WebServerFlow

from oauth2client.contrib import xsrfutil

from django.conf import settings

from .models import CredentialsModel

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest


def home(request):
    islands = Destination.objects.all().order_by('name')
    context_dict= {'islands': islands}
    return render(request, 'pinpoint/home.html', context=context_dict )

#def index(request):

  #  island_list = Destination.objects.order_by('name')
   # island = Destination.objects.all().order_by('name')
    
   # context_dict = {'islands': island_list, 'island': islands}

   # response = render(request, 'rango/home.html', context=context_dict)

   # return response

def booking(request):
    islands = Destination.objects.all().order_by('name')
    context_dict= {'islands': islands}
    return render(request, 'pinpoint/booking.html', context=context_dict )

def quiz(request):
    islands = Destination.objects.all().order_by('name')
    context_dict= {'islands': islands}
    return render(request, 'pinpoint/quiz.html', context=context_dict )

def destinations(request):
    islands = Destination.objects.all()
    context_dict= {'islands': islands}
    return render(request, 'pinpoint/destinations.html', context=context_dict)

def island_page(request):
    islands = Destination.objects.all().order_by('name')
    context_dict= {'islands': islands}
    return render(request, 'pinpoint/island_page.html', context=context_dict )


def show_island(request, destination_name_slug):
    islands = Destination.objects.all().order_by('name')
    destination_name_slug=destination_name_slug
    context_dict={'islands':islands, 'destination_name_slug':destination_name_slug,}
    return render(request, 'pinpoint/island_page.html', context=context_dict)

def register(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially. Code changes value to
    # True when registration succeeds.\
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()


            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)

            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.

            if 'picture' in request.FILES:

                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to indicate that the template
            # registration was successful.

            registered = True

        else:

            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)

    else:

        # Not a HTTP POST, so we render our form using two ModelForm instances.

        # These forms will be blank, ready for user input.

        user_form = UserForm()

        profile_form = UserProfileForm()

    # Render the template depending on the context.

    return render(request, 'pinpoint/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.

    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.

        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.

        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.

        if user:
            # Is the account active? It could have been disabled.

            if user.is_active:

                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.

                login(request, user)

                return HttpResponseRedirect(reverse('home'))

            else:
                # An inactive account was used - no logging in!

                return HttpResponse("Your Pinpoint account is disabled.")

        else:
            # Bad login details were provided. So we can't log the user in.

            print("Invalid login details: {0}, {1}".format(username, password))

            return HttpResponse("Invalid login details supplied.")



    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.

    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...

        return render(request, 'pinpoint/login.html', {})

@login_required
def restricted(request):

    return render(request, 'pinpoint/restricted.html', {})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.

    return HttpResponseRedirect(reverse('home'))

def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/restricted')

    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'pinpoint/edit_profile.html')


class AuthGoogleBeginView(View):
    def get(self, request):

        user = None

        if not request.user.is_anonymous():
            user = request.user

        storage = DjangoORMStorage(CredentialsModel, 'id', user, 'credential')
        credentials = storage.get()

        if credentials is None or credentials.invalid == True:
            FLOW.params['state'] = xsrfutil.generate_token(settings.GOOGLE_OAUTH2_CLIENT_SECRET,
                                                           request.user)
            authorize_url = FLOW.step1_get_authorize_url()

            return HttpResponseRedirect(authorize_url)

        return HttpResponseRedirect('/')


FLOW = OAuth2WebServerFlow(
    client_id=settings.GOOGLE_OAUTH2_CLIENT_ID,
    client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
    scope=settings.GOOGLE_OAUTH2_SCOPES,
    redirect_uri=settings.AUTH_REDIRECT_URL)

class AuthGoogleFinishedView(View):
    def get(self, request):
        # raise
        user = None
        if not request.user.is_anonymous():
            user = request.user

        if not xsrfutil.validate_token(
            settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            request.GET['state'].encode('UTF-8'),
            request.user
            ):

            return  HttpResponseBadRequest()

        credentials = FLOW.step2_exchange(request.GET)

        http = credentials.authorize(httplib2.Http())

        service_plus = discovery.build('plus', 'v1', http=http)

        person = service_plus.people().get(userId='me').execute()

        email = person ['emails'][0]['value']
        user, created = User.objects.get_or_create(username=email, email=email)
        user.is_active = True
        user.save()
        login(request, user)
        storage = DjangoORMStorage(CredentialsModel, 'id', user, 'credential')

        if storage.get() is None:
            storage.put(credentials)

        return HttpResponseRedirect('/')





        # first_name = person['name']['givenName']
        # last_name = person['name']['familyName']
        # user_image_url = person['image']['url']
        # user_language = person['language']
        # user_id = person['id']