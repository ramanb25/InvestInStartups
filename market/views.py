from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.http import Http404
from .models import onsale,ownership,transactions
from startup.models import StartupProfile
from investor.models import InvestorProfile
from django.shortcuts import render
from django.urls import reverse
from django.db.models import F
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from datetime import datetime

@login_required()
def getuser(username):
    try:
        user=User.objects.get(username=username)
        return user
    except:
        raise Exception('User Logged in error')

@login_required()
def check(request):
    user=getuser(request.user)
    if user.is_active:
        return 1
    else:
        raise Exception('User not active')

def isInvestor(user):
    try:
        profile=InvestorProfile.objects.get(user=user)
        if profile is not None:
            return 1
    except:
        return 0

@login_required
def index(request):
    #check(request)
    u = User.objects.get(username=request.user)
    if u.is_active:
        obj1=onsale.objects.all()
        obj2=transactions.objects.filter(buyer__username=request.user)
        obj3=transactions.objects.filter(owner__username=request.user)
        context={'list1':obj1,'user':request.user,'isinvestor':isInvestor(request.user),'bought':obj2,'sold':obj3}
        return render(request,'market/index.html',context)
    else:
        raise Exception('User not active')



#raman TODO Put loginreq everywhere
@login_required
def redirectSell(request):
	u = User.objects.get(username=request.user)
	up = StartupProfile.objects.filter(user=u)
	if(up.count()>0):
		return startupSell(request)
	up = InvestorProfile.objects.filter(user=u)
	if(up.count()>0):
		return investorSell(request)

def investorSell(request):
	u = User.objects.get(username=request.user)
	stockList=ownership.objects.filter(owner=u)
	context={'list':stockList}
	return render(request,'market/investorSell.html',context)

def startupSell(request):
    u = User.objects.get(username=request.user)
    stocklist = ownership.objects.filter(owner=u)
    
    context={'list':stocklist}
    return render(request,'market/startupSell.html',context)


def buy(request):
    u = User.objects.get(username=request.user)
    onsaleobj=onsale.objects.all().exclude(owner=u)
    context={'onsale':onsaleobj}
    return render(request,'market/buy.html',context)

@transaction.atomic
def execStartupSell(request):
    u = User.objects.get(username=request.user)
    startupObj = StartupProfile.objects.get(user=u)
    shareQty=int(request.POST['qty'+str(startupObj.stockName)])
    sharePrice=int(request.POST['price'+str(startupObj.stockName)])

    try:
        Seller_ownership=ownership.objects.get(owner=u,startup=startupObj)
        currentOnSaleStocks=onsale.objects.filter(owner=u,startup=startupObj)
        totalOnSaleTillNow=0
        for obj in currentOnSaleStocks:
            obj.delete()
        if Seller_ownership is None:
            raise Exception
        if Seller_ownership.sharepercentage<shareQty:
            raise Exception
        if Seller_ownership.sharepercentage<shareQty+totalOnSaleTillNow:
            raise Exception
    except:
        raise Exception

    onSaleObj=onsale(owner=u,startup=startupObj,stockpercentage=shareQty,stockprice=sharePrice)
    onSaleObj.save()
    return redirect('/app/')#index(request)

@transaction.atomic()
def execInvestorSell(request):
    u = User.objects.get(username=request.user)
    stockToSell=str(request.POST.get('choice'))
    startupObj=StartupProfile.objects.get(stockName=stockToSell)
    shareQty=int(request.POST['qty'+stockToSell])
    sharePrice=int(request.POST['price'+stockToSell])

    try:
        Seller_ownership=ownership.objects.get(owner=u,startup=startupObj)
        currentOnSaleStocks=onsale.objects.filter(owner=u,startup=startupObj)
        totalOnSaleTillNow=0
        for obj in currentOnSaleStocks:
            obj.delete()#totalOnSaleTillNow=totalOnSaleTillNow+obj.stockpercentage
        if Seller_ownership is None:
            raise Exception
        if Seller_ownership.sharepercentage<shareQty:
            raise Exception
        if Seller_ownership.sharepercentage<shareQty+totalOnSaleTillNow:
            raise Exception
    except:
        raise Exception

    
    onSaleObj=onsale(owner=u,startup=startupObj,stockpercentage=shareQty,stockprice=sharePrice)
    onSaleObj.save()
    return redirect('/app/')#index(request)



def isInvestor2(username):
    try:
        profile=InvestorProfile.objects.get(user__username=username)
        if profile is not None:
            return 1
    except:
        return 0

def getProfile(user):
    if(isInvestor(user)):
        return InvestorProfile.objects.get(user=user)
    return StartupProfile.objects.get(user=user)

def getProfile2(username):
    if(isInvestor2(username)):
        return InvestorProfile.objects.get(user__username=username)
    return StartupProfile.objects.get(user__username=username)

@transaction.atomic
def execBuy(request, context=None):
    #obj=stocks.objects.get(name=request.POST['choice'])

    buyer_user = User.objects.get(username=request.user)
    stockname,owner_username=request.POST['choice'].split()

    owner_user = getProfile2(owner_username).user
    startup_Profile=StartupProfile.objects.get(stockName=stockname)

    qtypurchase=float(request.POST['qty'+request.POST.get('choice')])

    if not isInvestor(buyer_user):
        raise Exception('You must be Investor')
    owner_onsale = onsale.objects.get(owner__username=owner_username, startup__stockName=stockname)
    try:
        owner_onsale=onsale.objects.get(owner__username=owner_username,startup__stockName=stockname)
        qtyonsale=owner_onsale.stockpercentage
        print 'raman'
        if qtyonsale is None:
            raise Exception('yo')
        typeOwner=isInvestor(owner_username)
    except:
        raise Exception("Not on sale")
    print(qtyonsale)
    print(qtypurchase)
    if qtyonsale<qtypurchase:
        raise Exception
    if qtypurchase<0:

        raise Exception
    ownerProfile=getProfile(owner_user)
    buyerProfile=getProfile(buyer_user)
    if ownerProfile is None:
        raise Exception
    if buyerProfile is None:
        raise Exception
    try:
        buyer_ownership=ownership.objects.get(owner=buyer_user,startup=startup_Profile)
    except:
        buyer_ownership=ownership()
        buyer_ownership.owner=buyer_user
        buyer_ownership.startup=startup_Profile
        buyer_ownership.sharepercentage=0
    owner_ownership=ownership.objects.get(owner=owner_user,startup=startup_Profile)
    buyer_ownership.sharepercentage=buyer_ownership.sharepercentage+qtypurchase
    owner_onsale.stockpercentage=owner_onsale.stockpercentage-qtypurchase
    owner_ownership.sharepercentage = owner_ownership.sharepercentage - qtypurchase

    buyer_ownership.save()
    print(buyer_ownership.sharepercentage)
    owner_ownership.save()
    owner_onsale.save()
    if(owner_onsale.stockpercentage==0):
        owner_onsale.delete()
    if (owner_ownership.sharepercentage == 0):
        owner_ownership.delete()
    transaction=transactions(owner=owner_user,buyer=buyer_user,stockpercentage=qtypurchase,stockprice=owner_onsale.stockprice,timestamp=datetime.now(),startup=startup_Profile)
    transaction.save()
    return redirect('/investor/')#render(request,'market/index.html',context)


#raman
# from .forms import UserForm, UserProfileForm

# def register(request):
#     # Like before, get the request's context.
#     context = RequestContext(request)

#     # A boolean value for telling the template whether the registration was successful.
#     # Set to False initially. Code changes value to True when registration succeeds.
#     registered = False

#     # If it's a HTTP POST, we're interested in processing form data.
#     if request.method == 'POST':
#         # Attempt to grab information from the raw form information.
#         # Note that we make use of both UserForm and UserProfileForm.
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)

#         # If the two forms are valid...
#         if user_form.is_valid() and profile_form.is_valid():
#             # Save the user's form data to the database.
#             user = user_form.save()

#             # Now we hash the password with the set_password method.
#             # Once hashed, we can update the user object.
#             user.set_password(user.password)
#             user.save()

#             # Now sort out the UserProfile instance.
#             # Since we need to set the user attribute ourselves, we set commit=False.
#             # This delays saving the model until we're ready to avoid integrity problems.
#             profile = profile_form.save(commit=False)
#             profile.user = user

#             # Now we save the UserProfile model instance.
#             profile.save()

#             # Update our variable to tell the template registration was successful.
#             registered = True

#         # Invalid form or forms - mistakes or something else?
#         # Print problems to the terminal.
#         # They'll also be shown to the user.
#         else:
#             print user_form.errors, profile_form.errors

#     # Not a HTTP POST, so we render our form using two ModelForm instances.
#     # These forms will be blank, ready for user input.
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()
#     print 'raman'
#     # Render the template depending on the context.
#     return render_to_response(
#             'app/register.html',
#             {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
#             context)

# def user_login(request):
#     # Like before, obtain the context for the user's request.
#     context = RequestContext(request)

#     # If the request is a HTTP POST, try to pull out the relevant information.
#     if request.method == 'POST':
#         # Gather the username and password provided by the user.
#         # This information is obtained from the login form.
#         username = request.POST['username']
#         password = request.POST['password']

#         # Use Django's machinery to attempt to see if the username/password
#         # combination is valid - a User object is returned if it is.
#         user = authenticate(username=username, password=password)

#         # If we have a User object, the details are correct.
#         # If None (Python's way of representing the absence of a value), no user
#         # with matching credentials was found.
#         if user:
#             # Is the account active? It could have been disabled.
#             if user.is_active:
#                 # If the account is valid and active, we can log the user in.
#                 # We'll send the user back to the homepage.
#                 login(request, user)
#                 return HttpResponseRedirect('/app/')
#             else:
#                 # An inactive account was used - no logging in!
#                 return HttpResponse("Your account is disabled.")
#         else:
#             # Bad login details were provided. So we can't log the user in.
#             print "Invalid login details: {0}, {1}".format(username, password)
#             return HttpResponse("Invalid login details supplied.")

#     # The request is not a HTTP POST, so display the login form.
#     # This scenario would most likely be a HTTP GET.
#     else:
#         # No context variables to pass to the template system, hence the
#         # blank dictionary object...
#         return render_to_response('app/login.html', {}, context)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return redirect('/app/')


# @login_required
# def restricted(request):
#     return HttpResponse("Since you're logged in, you can see this text!")


# @login_required
# def profile(request):
#     context = RequestContext(request)
#     u = User.objects.get(username=request.user)
#     up = UserProfile.objects.get(user=u)
#     context_dict ={ 'userprofile':up}
#     return render_to_response('app/profile.html', context_dict, context)