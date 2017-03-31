from django.http import HttpResponse
from django.http import Http404
from .models import Inv,accounts,uid,Sp,stocks,holdings
from django.shortcuts import render
from django.urls import reverse
from django.db.models import F
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	try:
		objs=Inv.objects.all()
		obj2=Sp.objects.all()
		context = {'list': objs, 'list2':obj2}
	except Sp.DoesNotExist:
		raise Http404("Object does not exist")
	return render(request,'app/index.html',context)

def forms(request):
	return render(request,'app/form.html')

def disp(request):
	try:
		obj=Inv.objects.filter(name=request.POST['name'])
		context={'list':obj}
	except Inv.DoesNotExist:
		raise Http404("Object does not exist")
	return render(request,'app/index.html',context)

def debit(request):
	try:
		obj=Inv.objects.get(name=request.POST['name'])
		obj2=Inv.objects.filter(name=request.POST['name'])

		context = {'list': obj2}
		objac=accounts.objects.get(accno=obj.accno.accno)
		objac.balance-=10
		
		objac.save()
		return render(request,'app/index.html',context)
	except Inv.DoesNotExist:
		raise Http404("Object does not exist")

def redirectBuy(request):
	obj=stocks.objects.all()
	context={'list':obj}
	return render(request,'app/buy.html',context)

def redirectSell(request):
	obj=stocks.objects.all()
	context={'list':obj}
	return render(request,'app/buy.html',context)


def execBuy(request):
	#obj=stocks.objects.get(name=request.POST['choice'])
	qty=int(request.POST['qty'+request.POST.get('choice')])
	if qty<0:
		raise Http404("Invalid Purchase Quantity")

	obj1=Sp.objects.get(name=request.POST.get('choice'))
	stocks.objects.filter(soName=obj1).update(shareCount=F('shareCount')-qty)
	stockObj=stocks.objects.get(soName=obj1)
	if(stockObj.shareCount<0):
		stocks.objects.filter(soName=obj1).update(shareCount=F('shareCount')+qty)
		raise Http404("Stock Limit Breached!")
	earning=stockObj.sharePrice*qty
	account=obj1.accno
	account.balance+=earning
	account.save()

	objs=Inv.objects.all()
	obj2=Sp.objects.all()
	context = {'list': objs, 'list2':obj2}
	return render(request,'app/index.html',context)


#raman
from .forms import UserForm, UserProfileForm

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
        user_form = UserForm()
        profile_form = UserProfileForm()
    print 'raman'
    # Render the template depending on the context.
    return render_to_response(
            'app/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


