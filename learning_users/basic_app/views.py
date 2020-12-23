from django.shortcuts import render
from basic_app.forms import userform,userprofileinfoform

from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import TaskForm
from django.shortcuts import redirect
from .models import Task






# Create your views here.
def index(request):
    # return HttpResponse("Hello World!!")
    form = TaskForm()
    if request.method == "POST":
        # Get the posted form
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")
    tasks = Task.objects.all() # add this
    return render(request, "basic_app/index.html", {"task_form": form, "tasks": tasks})




from django.shortcuts import render  
from django.http import HttpResponse  
from basic_app.functions import handle_uploaded_file  
from basic_app.forms import StudentForm  
def cool(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,"basic_app/cool.html",{'form':student})  




def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "basic_app/update_task.html", {"task_edit_form": form})






def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")




import os 
from pathlib import Path
import glob

from .models import names
from .forms import nameform
def AnalyticsView(request):
    form = nameform()
    if request.method == "POST":
        # Get the posted form
        form = nameform(request.POST)
        if form.is_valid():
            form.save()
        return redirect("show_pdf")
    tasks = names.objects.all() # add this

    #base_path = Path(__file__).parent
    #file_path = (base_path / "./pdf").resolve()
    #location = file_path
    location='./basic_app/pdf/'
    listn = []


    # r=>root, d=>directories, f=>files
    for r, d, f in os.walk(location):
        for item in f:
            listn.append(item)
    
    return render(request,'basic_app/show_pdf.html',context={'list':listn,"task_form": form, "tasks": tasks})


def update_task2(request, pk):
    task = names.objects.get(id=pk)

    form = nameform(instance=task)

    if request.method == "POST":
        form = nameform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_pdf")

    return render(request, "basic_app/update_task2.html", {"task_edit_form": form})






def delete_task2(request, pk):
    task = names.objects.get(id=pk)
    task.delete()
    return redirect("show_pdf")



from django.http import FileResponse, Http404
from basic_app.cool import open_pdf
def shownpdf(request):
    if request.method=='POST':
            global password
            password=request.POST.get('password')
            #print(password)    
            #open_pdf(password)
            password=str(password)
            #password=password.replace('pdf','jpg')
            ok={'cooll':password}
            try:
                return FileResponse(open('./basic_app/pdf/'+password, 'rb'), content_type='application/pdf')
            except FileNotFoundError:
                raise Http404()

    #return HttpResponseRedirect(reverse(AnalyticsView))
    #image_data = open("./basic_app/pdf/"+password, "rb").read()
    #return HttpResponse(image_data, content_type="image/png")


from basic_app.photo_delete import rem_photo

def del_pdf(request):
    if request.method=="POST":
        global deleter
        deleter=request.POST.get("password")
        #print('i'*10 + deleter)
        #print('cool')
        rem_photo(deleter)
    
    return HttpResponseRedirect(reverse(AnalyticsView))



from basic_app.pdf_rename import ren_pdf
def rename_pdf(request):
    if request.method=="POST":
        global renamer
        renamer=request.POST.get('renamer')
        renamed=request.POST.get('renamed')
        print('..............................')
        print(renamer)
        print(renamed)
        ren_pdf(renamer,renamed)
    return HttpResponseRedirect(reverse(AnalyticsView))







    
#extra speial page
@login_required
def special(request):
    return HttpResponse('you arte logged in,nice')



#extra login logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))





def register(request):
    registered=False
    if request.method=="POST":
        user_form=userform(data=request.POST)
        profile_form=userprofileinfoform(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=userform()
        profile_form=userprofileinfoform()
    return render(request,'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


# view for login page

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user :
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('account not active')
        else:
            print("someont tried to login and failed")
            print('Username:{} and password {}'.format(username,password))
            return HttpResponse('invalid login details supplied')
    else:
        return render(request,'basic_app/login.html',{})







from .models import Task1
from .forms import TaskForm1
def index1(request):
    # return HttpResponse("Hello World!!")
    form = TaskForm()
    if request.method == "POST":
        # Get the posted form
        form = TaskForm1(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index1")
    tasks = Task1.objects.all() # add this
    return render(request, "basic_app/index1.html", {"task_form": form, "tasks": tasks})




def update_task1(request, pk):
    task = Task1.objects.get(id=pk)

    form = TaskForm1(instance=task)

    if request.method == "POST":
        form = TaskForm1(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index1")

    return render(request, "basic_app/update_task1.html", {"task_edit_form": form})






def delete_task1(request, pk):
    task = Task1.objects.get(id=pk)
    task.delete()
    return redirect("index1")


