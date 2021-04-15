from django.contrib import admin
from .models import Student
from .models import Books
from .models import Lab
from .models import Faculty


admin.site.register(Student)
admin.site.register(Books)
admin.site.register(Lab)
admin.site.register(Faculty)