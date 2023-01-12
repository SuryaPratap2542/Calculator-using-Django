from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
# import django.contrib import admin
def calc(request):
    c=""
    n1=""
    n2=""
    op=""
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
    except:
        c="Invalid opr....."
    print(c)
    return render(request,"index.html",{'c':c,'n1':n1,'n2':n2,'op':op})

