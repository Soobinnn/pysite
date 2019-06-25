from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from guestbook.models import Guestbook

def index(request):
    guestbook = Guestbook.objects.all().order_by('-no')
    data = {'guestbook': guestbook}
    for t in guestbook:
        print(t)

    return render(request, 'guestbook/list.html', data)

def write(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.content = request.POST['content']

    guestbook.save()

    return HttpResponseRedirect('/guestbook/')

def deleform(request, no=0):
    data = {'no':no}
    return render(request, 'guestbook/deleteform.html', data)

def delete(request):
    check = Guestbook.objects.filter(no=request.POST['no']).filter(password=request.POST['password'])
    check.delete()

    return HttpResponseRedirect('/guestbook/')


def view(request):
    pass