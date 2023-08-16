from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    teams = Team.objects.all()
    return render(request,"index.html",{'result':obj,'res':teams})


#def result(request):
#    x=int(request.GET['num1'])
 #   y=int(request.GET['num2'])
  #  add=x+y
   # sub=x-y
    #mul=x*y
    #div=x/y
    #return render(request,"result.html",{'addition':add,'subtraction':sub,'multiplication':mul,'division':div})

#def contact(request):
 #   return HttpResponse("Am contact")

#def detail(request):
  #  return HttpResponse("This page shows the details")

#def thanks(request):
 #   return HttpResponse("Thankyou")