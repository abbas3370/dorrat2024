from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import login11,matiere,nstudent101,student101,anne,regeleve,stok,stok11,visamoy,mony,school,ps123note,regeleveps,mediaschool,videoschool,newsschool

# Register your models here.
mymodels=[login11, matiere,nstudent101,student101,anne,regeleve,stok,stok11,visamoy,mony,school,ps123note,regeleveps,mediaschool,videoschool,newsschool]
admin.site.register(mymodels)
