from django.http import HttpResponse
from django.http import Http404
from .models import Inv,accounts,uid,Sp
from django.shortcuts import render
from django.urls import reverse

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