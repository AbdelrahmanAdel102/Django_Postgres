from django.shortcuts import render, redirect
from .models import *


def home(request):
    return render(request, 'affairs/home.html')


def contactus(request):
    return render(request, 'affairs/contact.html')


def aboutUS(request):
    return render(request, 'affairs/about.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if Myuser.objects.filter(username=email, password=password).exists():
            return redirect('addStudent')
        else:
            return render(request, "affairs/login.html")
    else:
        return render(request, 'affairs/login.html')

def addUser(request):
    if (request.method == 'GET'):
        return render(request, 'affairs/register.html')
    else:
        email = request.POST['email']
        password = request.POST['password']
        Myuser.objects.create(username=email, password=password)
        return render(request, 'affairs/login.html')


def addStudent(request):
    if (request.method == 'GET'):
        return render(request, 'affairs/addStudents.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        Students.objects.create(name=name, email=email)
        return render(request, 'affairs/addStudents.html')

def viewStudent(request):
    context ={}
    data = Students.objects.all()
    context['Students'] = data
    return render(request,'affairs/viewStudent.html',context)

def deletestudent(request,id):
    context={}
    Students.objects.filter(id=id).delete()
    data = Students.objects.all()
    context['Students'] = data
    return render(request, 'affairs/viewStudent.html', context)

def updatestudent(request,id):
    if (request.method == 'GET'):
        context = {}
        Students.objects.filter(id=id)
        data = Students.objects.get(id=id)
        context['Student'] = data
        return render(request, 'affairs/updateStudent.html',context)
    else:
        name = request.POST['name']
        email = request.POST['email']
        Students.objects.filter(id=id).update(name=name,email=email)
        return redirect('viewStudent')
