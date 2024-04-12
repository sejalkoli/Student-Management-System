from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import csv
import datetime
from datetime import date
import re

# Create your views here.
# Home Page
def index(request):
    return render(request,"index.html")
    
## Student - Enquiry
def enquiry(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        contact = request.POST['contact']
        education = request.POST['education']
        department = request.POST['department']
        aadharno = request.POST['aadharno']
        clgname = request.POST['clgname']
        reference = request.POST['reference']
        date=datetime.datetime.now()
        date = date.strftime("%d/%m/%y")

        errors = []

        # Validate email format
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            errors.append('Invalid email format. Please enter a valid email address.')

         # Validate email uniqueness
        if Enquiry.objects.filter(email=email).exists():
            errors.append('Email is already registered.')

         # Validate phone number format
        if not re.match(r'^\d{10}$', contact):
            errors.append('Phone number must contain exactly 10 digits.')

         # Validate Aadhar number format
        if not re.match(r'^\d{12}$', aadharno):
            errors.append('Aadhar number must contain exactly 12 digits.')

        if len(password) < 8 or \
                not any(char.isdigit() for char in password) or \
                not any(char.isupper() for char in password) or \
                not any(char.islower() for char in password) or \
                not any(char in '!@#$%^&*()-_=+[]{};:,.<>?`~' for char in password):
                errors.append('Password doesn\'t meet the given criteria.')

        if errors:
            return render(request, 'enquiry.html', {'errors': errors})
        
        new_user = Enquiry(name=name, email=email,password=password,address=address,contact=contact,education=education,date = date,department=department,aadharno=aadharno,clgname=clgname,reference=reference)
        new_user.save()
        user = Enquiry.objects.all().filter(name=name,email=email,aadharno=aadharno).values_list()
        for i in user:
            for j in i:
                userid = i[0]
        courses = Courses.objects.filter(department=department).values()
        data = {
            "courses":courses,
            "userid":userid,
        }
        return render(request,'courses.html',data)
    else:
        return render(request,'enquiry.html')


def enroll(request,id):
    if request.method == "POST":
        user = Enquiry.objects.all().values_list().last() #  OUTPUT will be single tuple
        course = Courses.objects.all().filter(id=id).values_list() # <QuerySet [(17, 'Django', 'IT', '185000', 'Framework For Python')]>
        for i in course:
            department = i[2]
            course = i[1]
        userid = user[0]
        Enquiry.objects.all().filter(id=userid).update(department=department,course=course,enrl_status="Enrolled")
        return render(request,'stdlogin.html',{"msg":"Enrollment Successful"})
        
    else:
        course = Courses.objects.get(id=id)
        return render(request,'enroll.html',{"course":course,})


def upgrade(request,department,email):
    courses = Courses.objects.filter(department=department).values()
    return render(request,"upgrade.html",{'courses':courses,'email':email})
    

def add_course(request,id,email):
    add_course = Enquiry.objects.filter(email=email)
    cr = Courses.objects.filter(id=id).values('coursename').first()
    for i in add_course:
        i.course += str(" ") +str("+ ") + cr['coursename']
        i.save()
    users = Enquiry.objects.filter(email=email)
    if users.exists():
            login = users.first()
            return render(request,"stdresult.html",{'login':login})
    else:
            return render(request, 'stdlogin.html', {"msg": "Course cannot add"})

# student login
def stdlogin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        users = Enquiry.objects.filter(name=name, password=password)
        if users.exists():
            login = users.first()
            return render(request, "stdresult.html", {'login': login})
        else:
            return render(request, 'stdlogin.html', {"msg": "Login Unsuccessful"})
    return render(request, 'stdlogin.html')

## Admin
def host(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        hosts = Host.objects.all()
        for host in hosts:
            if username == host.username and password == host.password:
                return render(request, "admin_result.html")
        else:
            return HttpResponse("Login Unsuccessful")
    else:  # GET request
        return render(request, "adminlogin.html")
    
def admin_result(request):
    return render(request,"admin_result.html")   

# manage courses
def createcourse(request):
    if request.method == 'POST':
        department = request.POST['department']
        coursename = request.POST['coursename']
        fees = request.POST['fees']
        description = request.POST['description']

        create_course = Courses(department=department,coursename=coursename,fees=fees,description=description)
        create_course.save()
        if department == "IT":
            return redirect('/IT')
        elif department == "Mechanical":
            return redirect('/Mechanical')
        elif department == "Civil":
            return redirect('/Civil')
        else:
            return render(request,"managecourse.html")
    else:
        return render(request,"managecourse.html")

# Admin - edit course
def edit(request,id):
    courses = Courses.objects.get(id=id)
    form = CoursesForm(request.POST or None,instance = courses)
    if form.is_valid():
        form.save()
        department = form.cleaned_data['department']        
        if department == "IT":
            return redirect('/IT')
        elif department == "Civil":
            return redirect('/Civil')
        
        elif department == "Mechanical":
            return redirect('/Mechanical')
        else:
            return render(request,"managecourse.html")
    return render(request,"coursedit.html",{'courses':courses,'form':form})

# delete course
def destroy(request, id, department):
    course1 = Courses.objects.filter(id=id, department=department)
    course1.delete()  
    return redirect(f"/{department}")

def it(request):
    new_courses = Courses.objects.filter(department = "IT")
    return render(request,"managecourse.html",{'new_courses':new_courses})

def civil(request):
    new_courses = Courses.objects.filter(department = "Civil")
    return render(request,"managecourse.html",{'new_courses':new_courses})

def mechanical(request):
    new_courses = Courses.objects.filter(department = "Mechanical")
    return render(request,"managecourse.html",{'new_courses':new_courses})

def trainers(request):
    trainers = Trainers.objects.all()
    return render(request,"addtrainer.html",{'trainers':trainers})

# add Trainer 
def addtrainer(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        age = request.POST['age']

        add_trainer = Trainers(name=name,department=department,age=age)
        add_trainer.save()
        return redirect('/trainers')
    else:
        return render(request,"addtrainer.html")
    
# Edit trainers data
def traineredit(request,id):
    trainer = Trainers.objects.get(id=id)
    form = TrainersForm(request.POST or None,instance = trainer)
    if form.is_valid():
        form.save()
        return redirect('/trainers')
    return render(request,"traineredit.html",{'trainer':trainer,'form':form})

# delete trainers record
def tdelete(request, id):  
    trainer1 = Trainers.objects.get(id=id)  
    trainer1.delete()  
    return redirect("/trainers") 

# Admin - Filter todays & all Queries
def enquiries(request):
    today = datetime.datetime.now().date()
    formatted_today = today.strftime("%d/%m/%y")
    todays_enq = Enquiry.objects.filter(date=formatted_today)
    # d=datetime.datetime.now() #using this the default date - 2024-03-18 
    # date=date.strftime("%x")
    enquiries = Enquiry.objects.all()
    return render(request,"allenquiries.html",{'enquiries':enquiries,'todays_enq':todays_enq}) 

# dowload todays queries in csv file
def todays_enq(request):
    today = datetime.datetime.now().date()
    formatted_today = today.strftime("%d/%m/%y")
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment;filename="todays_enquiries.csv"'
    enqs = Enquiry.objects.filter(date = formatted_today )
    writer = csv.writer(response)
    for enq in enqs:
        writer.writerow([enq.name,enq.email,enq.contact,enq.address,enq.education,
                         enq.date,enq.department,enq.aadharno,enq.clgname,
                         enq.reference,enq.enrl_status,enq.course])
        # write.writerow([enq[1],enq[2]....])    # we can also write like this
    return response

# download all enquiries
def allenq(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment;filename="allenquiries.csv"'
    enqs = Enquiry.objects.all()
    writer = csv.writer(response)
    for enq in enqs:
        writer.writerow([enq.name,enq.email,enq.contact,enq.address,enq.education,
                         enq.date,enq.department,enq.aadharno,enq.clgname,enq.reference,
                         enq.enrl_status,enq.course])
    return response

# Admin - ToDo App
def todolist(request):
    todolist = ToDo.objects.all()
    return render(request,"todoapp.html",{'todolist':todolist})

def todo(request):
    if request.method == 'POST':
        type = request.POST['type']
        date = request.POST['date']
        description = request.POST['description']
        add_task = ToDo(type=type,date=date,description=description)
        add_task.save()
        return redirect('/todolist')
    else:
        return render(request,"todoapp.html")

def todoedit(request,id):
    todo = ToDo.objects.get(id=id)
    form = ToDoForm(request.POST or None,instance = todo)
    if form.is_valid():
        form.save()
        return redirect('/todolist')
    return render(request,"todoedit.html",{'todo':todo,'form':form})

def tododelete(request, id):  
    task1 = ToDo.objects.get(id=id)  
    task1.delete()  
    return redirect("/todolist") 

# Trainers
def trainers_login(request):
    if request.method == "POST":
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        trainer = Trainerslogin.objects.all()  
        
        for t in trainer:
            if username == t.username and password == t.password:  
                department = t.department
                students = Enquiry.objects.filter(department=department, enrl_status="Enrolled")
                context = {
                    'students': students,
                    'department': department,
                }
                return render(request, "trainers_result.html", context)
        
        return HttpResponse("Login Unsuccessful")
    
    else:
        return render(request, "trainerslogin.html")

