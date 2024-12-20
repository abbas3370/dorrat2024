from django import  forms

class loginform(forms.Form):
   username=forms.CharField(max_length=50)
   password=forms.CharField(max_length=50)


#model.objects.filter(field_1=x, field_2=y) 
##      path("courses/<slug:param1>/<slug:param2>", views.view_funct, name="double_slug")
##  path('app1/eleve1/updateliste/<str:cod008>/<str:xann1>/<str:xcla1>/<str:xsection1>/',views.updateliste,name='updlist'),
## 
#def updateliste(request, cod008, xann1, xcla1, xsection1):
# xann=request.POST.get('anne2002')
# print(xann)
# print(cod008)
# print(xann1)
# print(xcla1)
# print(xsection1)
# r=regeleve.objects.filter(code1=cod008, anne1=xann1)
# for ri in r :
#   ru=regeleve.objects.get(id=ri.id)
#   ru.classe1=xcla1
#   ru.section1=xsection1
#   ru.save()
# return HttpResponseRedirect(reverse('form10033'))

 #<div class='editLi'>
  #    <td><a href="updateliste/{{rec1.code}}/anne2002/classe2002/section2002"   style="background-color: gray;font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">تسجيل الطالب</a></t
  
from num2words import num2words
print(num2words(35,lang='arab'))

ax6="2024-2025"
n1=ax6[0:4]
n2=ax6[5:9]
i1=int(n1)
i2=int(n2)
cx1=num2words(i1,lang='arab')
cx2=num2words(i2,lang='arab')
print(cx1)