from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import DepartmentForm,ExhibitForm,AnimalForm,StaffForm

# Create your views here.
def home(request):
    return render(request,'Zoo/home.html',{})

def login_user(request):
    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,'Logged in successfully')
            return redirect('home')
        else:
            messages.success(request,'Failed to Log in! Try again...')
            return redirect('login')
    else:
        return render(request, 'Zoo/login.html', {})
def logout_user(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('home')

def add_department(request):
    if (request.method == 'POST'):
        form = DepartmentForm(request.POST)# instance=request.user)
        if(form.is_valid()):
            form.save(commit=True)
            messages.success(request, 'You have successfully added a record')
        else:
            print (form.errors)
    else:
        form = DepartmentForm()
    context = {'form':form}
    return render(request,'Zoo/add_department.html',context)

def add_exhibit(request):
    if (request.method == 'POST'):
        form = ExhibitForm(request.POST)# instance=request.user)
        if(form.is_valid()):
            form.save(commit=True)
            messages.success(request, 'You have successfully added a record')
        else:
            print (form.errors)
    else:
        form = ExhibitForm()
    context = {'form':form}
    return render(request,'Zoo/add_exhibit.html',context)

def add_animal(request):
    if (request.method == 'POST'):
        form = AnimalForm(request.POST)# instance=request.user)
        if(form.is_valid()):
            form.save(commit=True)
            messages.success(request, 'You have successfully added a record')
        else:
            print (form.errors)
    else:
        form = AnimalForm()
    context = {'form':form}
    return render(request,'Zoo/add_animal.html',context)
def add_staff(request):
    if (request.method == 'POST'):
        form = StaffForm(request.POST)# instance=request.user)
        if(form.is_valid()):
            form.save(commit=True)
            messages.success(request, 'You have successfully added a record')
        else:
            print (form.errors)
    else:
        form = StaffForm()
    context = {'form':form}
    return render(request,'Zoo/add_Staff.html',context)