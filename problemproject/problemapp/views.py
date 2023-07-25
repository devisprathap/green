from django.http import HttpResponse
from django .shortcuts import render

from .models import Place,Team


def demo(request):

    obj=Place.objects.all()

    ob=Team.objects.all()
    return render(request,"index.html",{'result':obj,'res':ob})


# def operation(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     a=x+y
#     b=x-y
#     c=x*y
#     d=x%y
#     return render(request,"result.html",{"addition":a,"subtraction":b,"multiplication":c,"division":d})

