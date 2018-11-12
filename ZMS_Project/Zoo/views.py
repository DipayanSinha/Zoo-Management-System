from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import DepartmentForm,ExhibitForm,AnimalForm,StaffForm,ChangePassword
from .models import Animal,Department,Staff,Exhibit
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    return render(request, 'Zoo/home.html', {})

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
        return render(request, 'Zoo/Authenticate/login.html', {})

@login_required(login_url='/login/')
def change_password(request):
    if (request.method == 'POST'):
        form = ChangePassword(data=request.POST,user=request.user)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'You have successfully changed your password')
            return redirect('home')
    else:
        form = ChangePassword(user=request.user)
    context = {'form': form}
    return render(request, 'zoo/Authenticate/change_password.html', context)

def logout_user(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('home')

@login_required()
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
    return render(request, 'Zoo/departments/add_department.html', context)

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
    return render(request, 'Zoo/exhibits/add_exhibit.html', context)

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
    return render(request, 'Zoo/animals/add_animal.html', context)
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
    return render(request, 'Zoo/staff/add_Staff.html', context)

def view_animals(request):
    animals = ""
    if (request.method == 'POST'):
        search_text = request.POST['search_text']
    else:
        search_text = ''
    animals = Animal.objects.filter(commonname__contains=search_text) or Animal.objects.filter(id__contains=search_text)
    return render(request, 'Zoo/animals/list_animals.html', {'animals': animals})

def animal_profile(request,id):
    key = Animal.objects.get(pk=id)
    context = {'key':key}
    return render(request, 'Zoo/animals/animal_profile.html', context)

def animal_delete(request, id):
    animal = Animal.objects.get(pk = id)
    animal.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('view_animals')

def edit_animal(request, id):
   animal = get_object_or_404(Animal, pk=id)
   if request.method == "POST":
       form = AnimalForm(request.POST, instance=animal)
       if form.is_valid():
          post = form.save(commit=True)
          post.save()
          return redirect('view_animals')
   else:
       form = AnimalForm(instance=animal)
   return render(request, 'Zoo/animals/edit_animal.html', {'form': form, 'animal':animal})

def deptList(request):
    depts = ""
    if (request.method == 'POST'):
        search_text = request.POST['search_text']
    else:
        search_text = ''
    depts = Department.objects.filter(name__contains=search_text) or Department.objects.filter(id__contains=search_text)
    return render(request, 'Zoo/departments/department_list.html', {'depts': depts})
    #depts = Department.objects.all().order_by('id')
    #return render(request,'Zoo/department_list.html',{'depts':depts})

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
   return render(request, 'Zoo/departments/edit_department.html', {'form': form, 'dept':department})

'''def search_department(request):
    depts=""
    if(request.method=='POST'):
        search_text = request.POST['search_text']
    else:
        search_text=''
    depts = Department.objects.filter(name__contains=search_text ) or Department.objects.filter(id__contains=search_text )
    return render(request,'Zoo/department_search.html',{'depts':depts})'''

def department_profile(request,id):
    key = Department.objects.get(pk=id)
    context = {'key':key}
    return render(request, 'Zoo/departments/department_profile.html', context)

def view_staff(request):
    if (request.method == 'POST'):
        search_text = request.POST['search_text']
    else:
        search_text = ''
    staff = Staff.objects.filter(firstname__contains=search_text) or Staff.objects.filter(id__contains=search_text)
    return render(request, 'Zoo/staff/staff_list.html', {'staff': staff})

def staff_profile(request,id):
    key = Staff.objects.get(pk=id)
    context = {'key':key}
    return render(request, 'Zoo/staff/staff_profile.html', context)

def staff_delete(request, id):
    staff = Staff.objects.get(pk = id)
    staff.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('staff_list')

def edit_staff(request, id):
   staff = get_object_or_404(Staff, pk=id)
   if request.method == "POST":
       form = StaffForm(request.POST, instance=staff)
       if form.is_valid():
          post = form.save(commit=True)
          post.save()
          return redirect('staff_list')
   else:
       form = StaffForm(instance=staff)
   return render(request, 'Zoo/staff/edit_staff.html', {'form': form, 'staff':staff})

def view_exhibit(request):
    if (request.method == 'POST'):
        search_text = request.POST['search_text']
    else:
        search_text = ''
    exhibit = Exhibit.objects.filter(name__contains=search_text) or Exhibit.objects.filter(id__contains=search_text)
    return render(request, 'Zoo/exhibits/exhibit_list.html', {'exhibits': exhibit})

def exhibit_profile(request,id):
    key = Exhibit.objects.get(pk=id)
    context = {'key':key}
    return render(request, 'Zoo/exhibits/exhibit_profile.html', context)

def exhibit_delete(request, id):
    exhibit = Exhibit.objects.get(pk = id)
    exhibit.delete()
    messages.success(request, 'Deleted successfully')
    return redirect('exhibit_list')

def edit_exhibit(request, id):
   exhibit= get_object_or_404(Exhibit, pk=id)
   if request.method == "POST":
       form = ExhibitForm(request.POST, instance=exhibit)
       if form.is_valid():
          post = form.save(commit=True)
          post.save()
          return redirect('exhibit_list')
   else:
       form = ExhibitForm(instance=exhibit)
   return render(request, 'Zoo/exhibits/edit_exhibit.html', {'form': form, 'exhibits':exhibit})

def animal_gallery(request):
    return render(request, 'Zoo/gallery/animal_gallery.html', {})
def bird_gallery(request):
    return render(request, 'Zoo/gallery/bird_gallery.html', {})
def aquatic_gallery(request):
    return render(request, 'Zoo/gallery/aquatic_gallery.html', {})
def sidebar(request):
    return render(request,'Zoo/Sidebar.html',{})
def test(request):
    return render(request, 'Zoo/home-2.html', {})