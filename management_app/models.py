from django.db import models

# Create your models here.

class Host(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    class Meta:
        db_table = "hosttable"
    def __str__(self):
        return f"{self.username}"

class Courses(models.Model):
    coursename = models.CharField(max_length = 50)
    department = models.CharField(max_length = 50)
    fees = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    class Meta:
        db_table = "courses"
    def __str__(self):
        return f"{self.coursename} {self.department}"
    
class Trainers(models.Model):
    name = models.CharField(max_length = 50)
    department = models.CharField(max_length = 50)
    age = models.CharField(max_length = 50)
    class Meta:
        db_table = "trainers"
    def __str__(self):
        return f"{self.name}"
    
class Trainerslogin(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    department = models.CharField(max_length = 50,null= True)
    class Meta:
        db_table = "trainers_login_table"
    def __str__(self):
        return f"{self.username}"
    
class Enquiry(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50,null= True)
    address = models.CharField(max_length = 50)
    contact = models.CharField(max_length = 50)
    education = models.CharField(max_length = 50)
    date = models.CharField(max_length = 50)
    department = models.CharField(max_length = 50,null= True)
    aadharno = models.CharField(max_length = 50,null= True)
    clgname = models.CharField(max_length = 50,null= True)
    reference = models.CharField(max_length = 50,null= True)
    enrl_status = models.CharField(max_length=50,default = "NO")
    course = models.CharField(max_length=50,default="Not Enroll Yet")
    class Meta:
        db_table = "enquiry"
    def __str__(self):
        return f"{self.name}"
    
class Attendance(models.Model):
    roll_no = models.CharField(max_length = 50,null = True)
    email = models.CharField(max_length = 50,null = True)
    name = models.CharField(max_length = 50,null = True)
    date = models.CharField(max_length = 50,null = True)
    status = models.CharField(max_length = 50,null = True)
    class Meta:
        db_table = "attendance"
    def __str__(self):
        return f"{self.name}"
    
class ToDo(models.Model):
    type = models.CharField(max_length = 50)
    date = models.DateField()
    description = models.CharField(max_length = 50)
    class Meta:
        db_table = "todo"