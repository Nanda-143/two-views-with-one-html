from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def Topic_insert(request):
    t=input('enter topic name : ')
    to=Topic.objects.get_or_create(topic_name=t)[0]
    to.save()
    return HttpResponse('data inserted')

def Webpage_insert(request):
    t=input('enter topic name : ')
    to=Topic.objects.get(topic_name=t)
    n=input('enter a name : ')
    u=input('enter url : ')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('data inserted')


def Access_insert(request):
    n=input('enter a name : ')
    no=Webpage.objects.get(name=n)
    a=input('enter author : ')
    e=input('enter a email : ')
    d=input('enter date : ')
    Ao=Access_record.objects.get_or_create(name=no,date=d,author=a,email=e)[0]
    Ao.save()
    return HttpResponse('data inserted')

qsto=Topic.objects.all()
t={'qsto':qsto}
def display_Topic(request):
    return render(request,'display_Topic.html',t)

qswo=Webpage.objects.all()
w={'qswo':qswo}
def display_Webpage(request):
    return render(request,'display_Webpage.html',w)

qsao=Access_record.objects.all()
a={'qsao':qsao}
def display_Access(request):
    return render(request,'display_access.html',a)


def insert_Topic(request):
    t=input('enter topic name : ')
    to=Topic.objects.get_or_create(topic_name=t)[0]
    to.save()
    qsto=Topic.objects.all()
    t={'qsto':qsto}
    return render(request,'display_Topic.html',t)

def insert_Webpage(request):
    t=input('enter topic name : ')
    to=Topic.objects.get(topic_name=t)
    n=input('enter a name : ')
    u=input('enter url : ')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    qswo=Webpage.objects.all()
    w={'qswo':qswo}
    return render(request,'display_Webpage.html',w)

def insert_Access(request):
    n=input('enter a name : ')
    no=Webpage.objects.get(name=n)
    a=input('enter author : ')
    e=input('enter a email : ')
    d=input('enter date : ')
    Ao=Access_record.objects.get_or_create(name=no,date=d,author=a,email=e)[0]
    Ao.save()
    qsao=Access_record.objects.all()
    a={'qsao':qsao}
    return render(request,'display_access.html',a)

