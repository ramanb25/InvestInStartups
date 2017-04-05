from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.http import Http404

from market.models import ownership
from startup.models import StartupProfile
from .models import InvestorProfile
#from app.models import accounts,uid
#from startup.models import StartupProfile
from django.shortcuts import render
from django.urls import reverse
from django.db.models import F
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User

#TODO dont redirect
@login_required()
def index(request):
    context=None
    if request.user.is_authenticated():
        u = User.objects.get(username=request.user)
        try:
            up = InvestorProfile.objects.get(user=u)
            my_ownership=None
            my_ownership=ownership.objects.filter(owner=u)
            startups=StartupProfile.objects.all()
            if up is not None:
                context = {'userprofile': up, 'user': u,'my_ownership':my_ownership,'startups':startups}
        except:
            raise Http404("You are on wrong portal Log in as different user to acccess this page")

    return render(request,'investor/index.html',context)



#raman
from .forms import InvestorProfileForm,InvestorUserForm

@transaction.atomic
def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = InvestorUserForm(data=request.POST)
        profile_form = InvestorProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = InvestorUserForm()
        profile_form = InvestorProfileForm()
    # Render the template depending on the context.
    return render_to_response(
            'investor/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

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
                return HttpResponseRedirect('/market/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('investor/login.html', {}, context)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/app/')


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


@login_required
def profile(request):
    context = RequestContext(request)
    u = User.objects.get(username=request.user)
    up = InvestorProfile.objects.get(user=u)
    context_dict ={ 'userprofile':up}
    return render_to_response('investor/profile.html', context_dict, context)