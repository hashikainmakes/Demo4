from django.http import HttpResponse
from django.shortcuts import render
from.models import Place,Team
# Create your views here.

def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()

    return render(request,"index1.html",{'result':obj,'results':obj1},)
#def addition(request):
 #   x = int(request.GET['num1'])
  #  y = int(request.GET['num2'])
   # res = x + y
    #res1 = x - y
   # res2 = x * y
   # res3 = x // y
   # return render(request, "about.html", {'add': res, 'sub': res1, 'mul': res2, 'div': res3})