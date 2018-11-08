from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import DepartmentForm,ExhibitForm,AnimalForm,StaffForm
from .models import Animal,Department

from django.shortcuts import get_list_or_404, get_object_or_404
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

def view_animals(request):
    query_results = Animal.objects.all()
    print(query_results)
    context = {'query_results':query_results}
    return render(request,'Zoo/list_animals.html',context)

def deptList(request):
    depts = Department.objects.all().order_by('id')
    return render(request,'Zoo/department_list.html',{'depts':depts})

def delete(request, id):
    department = Department.objects.get(pk = id)
    department.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('department_list')
    #return render(request,'Zoo/department_list.html',{'depts':depts})

def edit_department(request, id):
   department = get_object_or_404(Department, pk=id)
   if request.method == "POST":
       form = DepartmentForm(request.POST, instance=department)
       if form.is_valid():
          post = form.save(commit=True)
          post.save()
          return redirect('department_list')
   else:
       form = DepartmentForm(instance=department)
   return render(request, 'Zoo/edit_department.html', {'form': form,'dept':department})

def search_department(request):
    depts=""
    if(request.method=='POST'):
        search_text = request.POST['search_text']
    else:
        search_text=''
    depts = Department.objects.filter(name__contains=search_text )
    return render(request,'Zoo/department_search.html',{'depts':depts})


def profile(request,id):
    key = Department.objects.get(pk=id)
    context = {'key':key}
    return render(request,'Zoo/profile.html',context)

def sidebar(request):
    return render(request,'Zoo/Sidebar.html',{})
def test(request):
    return render(request, 'Zoo/test.html', {})