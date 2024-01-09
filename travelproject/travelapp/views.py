from django.http import HttpResponse
from django.shortcuts import render

from .models import place
from .models import team


# Create your views here.
# def demo(request):
#     return HttpResponse("helloworld")

# def demo(request):
#     name='India'
#     return render(request,"home.html",{'obj':name})

def demo(request):
     obj=place.objects.all()
     obj2 = team.objects.all()
     return render(request,"index.html",{'result':obj,'res':obj2})

# def operations(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     add=x+y
#     sub=x-y
#     mul=x*y
#     if y!=0:
#         div=x/y
#     else:
#         div="divisionbyzeroerror"
#     return render(request,"result.html",{'result':{"addition":add,"subtraction":sub,"multiplication":mul,"division":div}})
