from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    roll_no = models.CharField(max_length=5)
    degree = models.CharField(max_length=5,default='')
    year = models.CharField(max_length=5)
    batch = models.CharField(max_length=10)
    branch = models.CharField(max_length=5)
    secondary_edu = models.CharField(max_length=30)
    higher_edu = models.CharField(max_length=30)
    Address = models.CharField(max_length= 10)
    topper = models.BooleanField()
    stu_about = models.CharField(max_length=400)
    contact = models.EmailField(max_length=40)
    image = models.ImageField(upload_to="brcm/images",default='')
    def __str__(self):
        return self.first_name
class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=40)
    auth_name = models.CharField(max_length=50)
    year_of_pub = models.IntegerField()
    no_of_books = models.IntegerField()
    books_issued = models.IntegerField()
    issue_by = models.CharField(max_length=40)
    branch = models.CharField(max_length=5)
    image = models.ImageField(upload_to="brcm/images",default='')
    def __str__(self):
        return self.book_name
class Lab(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_name = models.CharField(max_length=50)
    block = models.CharField(max_length=2)
    floor_plan = (
        ('0', 'Ground'),
        ('1', 'First'),
        ('2', 'Second'),
    )
    floor = models.CharField(max_length=1, choices=floor_plan)
    room_no = models.CharField(max_length=10)
    def __str__(self):
        return self.lab_name
class Faculty(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)
    Qualification = models.CharField(max_length=50)
    Specialization	=  models.CharField(max_length=50)
    Branch = models.CharField(max_length=30)
    Experience =	 models.CharField(max_length=30)
    Email_ID =  models.CharField(max_length=40)
    Research_Publications =  models.IntegerField()	
    image = models.ImageField(upload_to="brcm/images",default='')
    def __str__(self):
        return self.name
