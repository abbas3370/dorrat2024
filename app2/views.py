from django.shortcuts import render
from .models import note,student
# Create your views here.
def note001(request):
     fff = note.objects.all()
     rr = fff.exclude(chimie=13.20)
     yyy = rr.exclude(math=2)
     return render(request, 'temapp2/note.html', {'reco1':str (yyy.count()) })

 
def note1(request):
     ttt = "chimie"
     yyy = note.objects.all()
     return render(request, 'temapp2/note1.html', {'reco':yyy.order_by(ttt)})


def name001(request):
     fff = note.objects.all()
     nnn=[9,10]
     xx= {'reco': fff.filter(math__range=[9,10])}
     return render(request, 'temapp2/note005.html', xx)


def photo001(request):
     fff = student.objects.all()
     nnn="ccc"
     xx= {'reco001': fff.filter(tname =nnn)}
     return render(request, 'temapp2/note003.html', xx)

def form001 (request):
    return render(request,'temapp2/form1.html')


