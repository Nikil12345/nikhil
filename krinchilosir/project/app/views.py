from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def dis(request):
    return render(request,'register.html')

def varrule(request,n):
    return HttpResponse("my number : "+(n))

def eve(request,n):
    if n%2==0:
        return HttpResponse("even :"+str(n))

def home(request):

    return render(request,"home.html")

"""def contact(request):
    if request.method=="POST" :
        y = request.POST['n2']
        return render(request,"contact.html",{"name":y})
    else:
        return render(request, "contact.html")"""

def contact(request,t):
    if request.method=="POST" :
        x = int(request.POST['n1'])
        y = int(request.POST['n2'])
        z = x+y

        return render(request,"home.html",{"name":z , "a" :"sum is"})
    else:
        return render(request, "contact.html")

def fainal(request):
    return render(request,"fainal.html")

def task(request):
    if request.method=='POST':
        x = int(request.POST['nu1'])
        y = int(request.POST['nu2'])
        z = x + y
        return render(request, "task.html", {"name": z, "a": "SUM = "})
    else:
        return render(request, "task.html")


def task2(request):
    if request.method == 'POST':
        w = int(request.POST['nu1'])
        x = int(request.POST['nu2'])
        y = int(request.POST['nu3'])
        if w>x and w>y:
            return render(request, "task2.html", {"name": w, "a": "GREATER = "})
        elif y>x and y>w :
            return render(request, "task2.html", {"name": y, "a": "GREATER = "})
        else:
            return render(request, "task2.html", {"name": x, "a": "GREATER = "})
    else:
        return render(request, "task2.html")

def task3(request):
    if request.method == 'POST':
        x = request.POST['str']
        s = ""
        for i in x:
            s = i + s
        if s == x:
            return render(request, "task3.html", {"name": x, "a": "YES...PALIDROME = "})
        else:
            return render(request, "task3.html", {"name": x, "a": "NOT...PALIDROME = "})
    else:
        return render(request, "task3.html")

def task4(request):
    if request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        l = []
        for i in range(x,y+1):
            l.append(i)
        return render(request, "task4.html", {"name": l})

    else:
        return render(request,"task4.html")

def task5(request):
    if request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        l=[]
        for i in range(1, y + 1):
            z = i * x
            f=str(i)+" X "+str(x)+" = "+str(z)
            l.append(f)
        return render(request, "task5.html", {"name" :l})
    else:
        return render(request, "task5.html")

def task6(request):
    if request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        l = []
        for i in range(x, y + 1):
            c=0
            for j in range(1,i+1):
                if i%j==0:
                    c = c+1
            if c==2:
                l.append(i)
        return render(request, "task6.html", {"na": l})
    else:
        return render(request, "task6.html")

# d={
#     1:[101,"ammu"],
#     2:[102,"kiran"],
#     3:[103,"manu"],
# }
# x=d.keys()
# def key(request):
#     return render(request,"key.html",{"key":x})
# def values(request,v):
#
#     y=d.values()
#     for j in y:
#         for i in x:
#             if v==i[0]:
#                 return render(request,"value.html",{"val":j[0]})
#             if v==i[1]:
#                 return render(request, "value.html", {"val": j[1]})
#             if v==i[2]:
#                 return render(request, "value.html", {"val": j[2]})
#             else:
#                 return render(request, "value.html")

def task7(request):
    if request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        l = []
        for i in range(y,x-1,-1):
            if i %2 != 0:
                l.append(i)
        return render(request, "task7.html", {"na": l})
    else:

        return render(request, "task7.html")




def register(request):
    if request.method == 'POST':
        a = request.POST['n1']
        b = request.POST['n2']
        c = request.POST['n3']
        d = request.POST['n4']
        data = student.objects.create(roll=a,name=b,age=c,mark=d)
        # data = student(roll=a, name=b, age=c, mark=d)
        data.save()
        return HttpResponse("Created")

def disp(request):
    if request.method == 'GET':
        data = student.objects.all()
        return render(request,'display.html',{'r':data})