
from django.contrib import admin
from .models import student,note
# Register your models here.
myModels=[student,note]
admin.site.register(myModels)
