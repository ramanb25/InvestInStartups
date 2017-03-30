from django.http import HttpResponse
from django.http import Http404
from .models import Inv,accounts,uid,Sp,stocks,holdings
from django.shortcuts import render
from django.urls import reverse
from django.db.models import F

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
	objs=Inv.objects.all()
	obj2=Sp.objects.all()
	context = {'list': objs, 'list2':obj2}
	return render(request,'app/index.html',context)



