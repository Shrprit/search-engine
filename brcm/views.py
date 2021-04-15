from django.shortcuts import render
from django.db.models import Q
from .models import Student
from .models import Books
from .models import Lab
from .models import Faculty

# Create your views here.
def index(request):
    return render(request,'search_engine/index.html')
def events(request):
    return render(request,'search_engine/events.html')
def news(request):
    return render(request,'search_engine/brknews.html')
def about(request):
    return render(request,'search_engine/brcm.html')
def search(request):
    query = request.GET.get('search')
    students =Student.objects.filter(
        Q(first_name__icontains = query) | Q(last_name__icontains= query ) | Q(branch__icontains=query) 
        |  Q(year__icontains = query) | Q(stu_about__icontains = query) | Q(roll_no__icontains=query) 
    )
    teachers =Faculty.objects.filter(
        Q(name__icontains = query)  | Q(Branch__icontains=query) | Q(designation__icontains = query)
    )
   
    book =Books.objects.filter(
        Q(book_name__icontains = query) | Q(auth_name__icontains= query ) | Q(branch__icontains=query)
    )
    labs =Lab.objects.filter(
        Q(lab_name__icontains = query) | Q(room_no__icontains= query ) | Q(floor=query) 
    )
    return render(request,'search_engine/search.html',{'students':students,'book':book,'teachers':teachers,'labs':labs})
def studentview(request,s_roll_no):
    student=Student.objects.filter(roll_no=s_roll_no)  
    return render(request,'search_engine/studentview.html',{'student':student[0]})
def bookview(request,bookname):
    book=Books.objects.filter(book_name=bookname)  
    return render(request,'search_engine/bookview.html',{'book':book[0]})
def teacherview(request,teachername):
    teach=Faculty.objects.filter(name=teachername)  
    return render(request,'search_engine/teacherview.html',{'teach':teach[0]})

