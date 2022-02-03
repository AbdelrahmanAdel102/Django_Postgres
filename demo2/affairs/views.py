from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from .forms import AddStudentsForm,AddStudentModel
from django.views import View


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
        my_user = Myuser.objects.filter(username=email, password=password).exists()
        admin_usr = authenticate(username=email, password=password)
        if my_user and admin_usr is not None:
            request.session['username']=request.POST['email']
            authlogin(request,admin_usr)
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
        ##Must Check if exists First in db before insert ==> not complated yet
        Myuser.objects.create(username=email, password=password)
        User.objects.create_user(username=request.POST['email'],password=request.POST['password'],is_staff=True)
        return redirect('')

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

def user_logout(request):
    request.session.clear()
    return redirect("")

### Day 3 ###
def addStudentForm(request):
    context = {}
    form = AddStudentsForm()
    if(request.method=='GET'):
        context['form'] = form
        return render(request,'affairs/addStudentForm.html',context)
    else:
        print(request.POST)
        Students.objects.create(name=request.POST['name'],email=request.POST['email'])
        # return render(request,'affairs/addStudentForm.html')
        return redirect('viewStudent')


def addStudentModel(request):
    context = {}
    form = AddStudentModel
    if (request.method=='GET'):
        context['MODEL'] = form
        return render(request, 'affairs/addStudentModel.html',context)
    else:
        form=AddStudentModel(request.POST)
        form.save()
        return redirect('viewStudent')

