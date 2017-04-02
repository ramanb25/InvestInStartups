from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import Http404
from .models import onSaleStartup,onSaleInvestor,holdings
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

def index(request):
    obj1=onSaleStartup.objects.all()
    obj2=onSaleInvestor.objects.all()
    context={'list1':obj1,'list2':obj2}
    return render(request,'market/index.html',context)

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
	investorObj = InvestorProfile.objects.get(user=u)
	stockList=holdings.objects.filter(investor=investorObj)
	context={'list':stockList}
	return render(request,'market/investorSell.html',context)

def startupSell(request):
    u = User.objects.get(username=request.user)
    startupObj = StartupProfile.objects.filter(user=u)
    
    context={'list':startupObj}
    return render(request,'market/startupSell.html',context)


def buy(request):
	onsaleinvestor=onSaleInvestor.objects.all()
	onsalestartup=onSaleStartup.objects.all()

	context={'startup':onsalestartup,'investor':onsaleinvestor}

	return render(request,'market/buy.html',context)

def execStartupSell(request):
    u = User.objects.get(username=request.user)
    startupObj = StartupProfile.objects.get(user=u)
    shareQty=int(request.POST['qty'+str(startupObj.stockName)])
    sharePrice=int(request.POST['price'+str(startupObj.stockName)])
    onSaleObj=onSaleStartup(holdings2=startupObj,shareCount=shareQty,sharePrice=sharePrice)
    onSaleObj.save()
    return index(request)

def execInvestorSell(request):
    u = User.objects.get(username=request.user)
    investorObj = InvestorProfile.objects.get(user=u)
    stockToSell=str(request.POST.get('choice'))
    startupObj=StartupProfile.objects.get(stockName=stockToSell)
    shareQty=int(request.POST['qty'+stockToSell])
    sharePrice=int(request.POST['price'+stockToSell])
    holdingsObj=holdings.objects.get(investor=investorObj,startup=startupObj)
    onSaleObj=onSaleInvestor(holdings1=holdingsObj,shareCount=shareQty,sharePrice=sharePrice)
    onSaleObj.save()
    return index(request)


	# def forms(request):
#     return render(request,'app/form.html')

# def disp(request):
#     try:
#         obj=InvestorProfile.objects.filter(user__username=request.POST['name'])
#         context={'list':obj}
#     except InvestorProfile.DoesNotExist:
#         raise Http404("Object does not exist")
#     return render(request,'app/index.html',context)

# def debit(request):
#     try:
#         obj=InvestorProfile.objects.get(user__username=request.POST['name'])
#         obj2=InvestorProfile.objects.filter(user__username=request.POST['name'])

#         context = {'list': obj2}
#         objac=accounts.objects.get(accno=obj.accno.accno)
#         objac.balance-=10

#         objac.save()
#         return render(request,'app/index.html',context)
#     except InvestorProfile.DoesNotExist:
#         raise Http404("Object does not exist")

# def redirectBuy(request):
#     obj=stocks.objects.all()
#     context={'list':obj}
#     return render(request,'app/buy.html',context)

# def redirectSell(request):
#     obj=stocks.objects.all()
#     context={'list':obj}
#     return render(request,'app/buy.html',context)


def execBuy(request, context=None):
    #obj=stocks.objects.get(name=request.POST['choice'])
    qty=int(request.POST['qty'+request.POST.get('choice')])
    type=int(request.POST['type'])
    if qty<0:
        raise Http404("Invalid Purchase Quantity")
    if type==1:
        #Investor TODO multiple price for same stock?
        obj1=onSaleInvestor.objects.get(holdings1__investor__user_username=request.POST.get('username'))
        #TODO add money to investor subtract from user
    else:
        #startup
        obj1 = onSaleStartup.objects.get(holdings2__startupName=request.POST.get('username'))
        #TODO add money to startup subtract from user
        user=request.user
        user.shareCount=user.shareCount-qty
        if(user.shareCount<0):
            raise Exception
        #Update on salestartup sharecount
        obj1.shareCount=obj1.shareCount-qty
        if (obj1.shareCount < 0):
            raise Exception
        elif (obj1.shareCount == 0):
            obj1.delete()
        else:
            obj1.save()
        #TODO add money to users holding of this startup

    #obj1=StartupProfile.objects.get(user__username=request.POST.get('choice'))
    # stocks.objects.filter(startup=obj1).update(shareCount=F('shareCount')-qty)
    # stockObj=stocks.objects.get(startup=obj1)
    if(obj1.shareCount<0):
        #TODO WHYstocks.objects.filter(startup=obj1).update(shareCount=F('shareCount')+qty)
        raise Http404("Stock Limit Breached!")
    #earning=obj1.sharePrice*qty
    #account=obj1.accno
    # account.balance+=earning
    # account.save()
    # print obj1
    # 
    # objs=InvestorProfile.objects.all()
    # obj2=StartupProfile.objects.all()
    # context = {'list': objs, 'list2':obj2}
    return render(request,'app/index.html',context)


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


# @login_required
# def user_logout(request):
#     # Since we know the user is logged in, we can now just log them out.
#     logout(request)

#     # Take the user back to the homepage.
#     return HttpResponseRedirect('/app/')


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