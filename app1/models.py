
from django.db import models

# Create your models here.
class login11(models.Model):
  username=models.CharField(max_length=50)
  password=models.CharField(max_length=50)



class newsschool(models.Model):
 id=models.AutoField(primary_key=True)
 dat=models.DateField()
 news1=models.TextField()
 rem1=models.CharField(max_length=50,null=True)
 rem2=models.CharField(max_length=50,null=True)


class mediaschool(models.Model):
 id=models.AutoField(primary_key=True)
 dat=models.DateField()
 image = models.ImageField(upload_to='static/image/',null=True)
 rem1=models.CharField(max_length=50,null=True)
 rem2=models.CharField(max_length=50,null=True)
 rem3=models.CharField(max_length=50,null=True)
 

class videoschool(models.Model):
 id=models.AutoField(primary_key=True)
 dat=models.DateField()
 video=models.FileField(upload_to='static/image/',null=True)
 rem1=models.CharField(max_length=50,null=True)
 rem2=models.CharField(max_length=50,null=True)
 rem3=models.CharField(max_length=50,null=True)

class ps123note(models.Model):
  id=models.AutoField(primary_key=True)
  anne=models.CharField(max_length=50)
  classe=models.CharField(max_length=50)
  groupe=models.CharField(max_length=100)
  champ=models.CharField(max_length=100)
  souschamp=models.CharField(max_length=300)
  rem1=models.CharField(max_length=100)
  rem2=models.CharField(max_length=50)
  rem3=models.CharField(max_length=50)
  num1=models.IntegerField("10")
  num2=models.IntegerField("10")


class school(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=50)
  numeducation=models.CharField(max_length=50)
  directeur=models.CharField(max_length=50)
  tasnif=models.CharField(max_length=50)
  fax=models.CharField(max_length=50)
  tel=models.CharField(max_length=50)
  tarhis=models.CharField(max_length=50)
  mohafaza=models.CharField(max_length=50)
  kadaa=models.CharField(max_length=50)
  city=models.CharField(max_length=50)
  rem1=models.CharField(max_length=50)
  rem2=models.CharField(max_length=50)
  num1=models.IntegerField("10")
  num2=models.IntegerField("10")
  imag=models.ImageField(upload_to='photos/%y/%m/%d')
  
# visamony هذا لكي يسمح المدير  برؤية معدلات الطلاب  بالنسبة للأهل
class visamoy(models.Model):
  id=models.AutoField(primary_key=True)
  visamoye=models.CharField(max_length=50)
 
class mony(models.Model):
  id=models.AutoField(primary_key=True)
  classe=models.CharField(max_length=50)
  anne=models.CharField(max_length=50)
  amountll=models.DecimalField(max_digits=12 , decimal_places=2)
  amountdd=models.DecimalField(max_digits=12 , decimal_places=2)
  tl=models.CharField(max_length=50)
  td=models.CharField(max_length=50)
##  stok  فيها كلمات سر المعلمين والسجل الاول دائما صاحب id=1 هو للادارة للعمل عليه خلال البرنامج  
class stok(models.Model):
  id=models.AutoField(primary_key=True)
  user=models.CharField(max_length=50)
  name=models.CharField(max_length=50)
  f1=models.CharField(max_length=50)
  f2=models.CharField(max_length=50) 

class stok11(models.Model):
  id=models.AutoField(primary_key=True)
  temp=models.CharField(max_length=50)  #  mois
  anne=models.CharField(max_length=50)
  classe=models.CharField(max_length=50)
  section=models.CharField(max_length=50)
 

class matiere(models.Model):
  id=models.AutoField(primary_key=True)
  code=models.CharField(max_length=50)
  nommatiere=models.CharField(max_length=50) 
  classe=models.CharField(max_length=50)
  section=models.CharField(max_length=50)
  anne=models.CharField(max_length=50)
  score=models.IntegerField()
####  a rejetter  ca
class nstudent101(models.Model):
  code=models.TextField(max_length=50)
  nom=models.TextField(max_length=50)
  pere=models.TextField(max_length=50)
  famille=models.TextField(max_length=50)
  

class student101(models.Model):
  id=models.AutoField(primary_key=True)
  code=models.CharField(max_length=50)
  nom=models.CharField(max_length=50)
  pere=models.CharField(max_length=50)
  famille=models.CharField(max_length=50)
  mere=models.CharField(max_length=50)
  city=models.CharField(max_length=50)
  tel=models.CharField(max_length=50)
  lieu=models.CharField(max_length=50)
  segel=models.CharField(max_length=50)
  dat=models.DateField()
  rem1=models.CharField(max_length=50)
  rem2=models.CharField(max_length=50)  # rem2 : كود الاب
  num1=models.IntegerField("10")
  num2=models.IntegerField("10")
  quit=models.CharField(max_length=50)

class logindirect(models.Model):
  username=models.CharField(max_length=50)
  password=models.CharField(max_length=50)
  
class anne(models.Model):
  id=models.AutoField(primary_key=True)
  ida=models.CharField(max_length=20)
  anne=models.CharField(max_length=50)

class regeleve(models.Model):
  id=models.AutoField(primary_key=True)
  code1=models.CharField(max_length=50)
  nom1=models.CharField(max_length=50)
  pere1=models.CharField(max_length=50)
  famille1=models.CharField(max_length=50)
  anne1=models.CharField(max_length=50)
  mois=models.CharField(max_length=50)
  classe1=models.CharField(max_length=50)
  section1=models.CharField(max_length=50)
  math=models.DecimalField(max_digits=7 , decimal_places=2)
  physique=models.DecimalField(max_digits=7 , decimal_places=2) 
  chimie=models.DecimalField(max_digits=7 , decimal_places=2) 
  bio=models.DecimalField(max_digits=7 , decimal_places=2) 
  arab1=models.DecimalField(max_digits=7 , decimal_places=2) 
  arab2=models.DecimalField(max_digits=7 , decimal_places=2) 
  arab3=models.DecimalField(max_digits=7 , decimal_places=2) 
  francais1=models.DecimalField(max_digits=7 , decimal_places=2)  
  francais2=models.DecimalField(max_digits=7 , decimal_places=2) 
  francais3=models.DecimalField(max_digits=7 , decimal_places=2) 
  eng =models.DecimalField(max_digits=7 , decimal_places=2) 
  civisme=models.DecimalField(max_digits=7 , decimal_places=2) 
  historique=models.DecimalField(max_digits=7 , decimal_places=2) 
  geographie=models.DecimalField(max_digits=7 , decimal_places=2) 
  economie=models.DecimalField(max_digits=7 , decimal_places=2) 
  socialite=models.DecimalField(max_digits=7 , decimal_places=2) 
  philosophie=models.DecimalField(max_digits=7 , decimal_places=2) 
  informatique=models.DecimalField(max_digits=7 , decimal_places=2) 
  religieu=models.DecimalField(max_digits=7 , decimal_places=2)
  art=models.DecimalField(max_digits=7 , decimal_places=2) 
  sport=models.DecimalField(max_digits=7 , decimal_places=2) 
  pass1=models.DecimalField(max_digits=7 , decimal_places=2)
  som1=models.DecimalField(max_digits=10 , default=0,decimal_places=2,null=True)
  som2=models.DecimalField(max_digits=7 , decimal_places=2)
     
     
class regeleveps(models.Model):
  id=models.AutoField(primary_key=True)
  code1=models.CharField(max_length=50)
  nom1=models.CharField(max_length=50)
  pere1=models.CharField(max_length=50)
  famille1=models.CharField(max_length=50)
  anne1=models.CharField(max_length=50)
  mois=models.CharField(max_length=50)
  classe1=models.CharField(max_length=50)
  section1=models.CharField(max_length=50)
  groupe=models.CharField(max_length=100)
  champ=models.CharField(max_length=100)
  souschamp=models.CharField(max_length=300)
  rem11=models.CharField(max_length=100)
  rem21=models.CharField(max_length=50)
  rem31=models.CharField(max_length=50)
  num11=models.IntegerField("10")
  num21=models.IntegerField("10")
  sem1=models.CharField(max_length=50)
  sem2=models.CharField(max_length=50)
  sem3=models.CharField(max_length=50)
  sem4=models.CharField(max_length=50)
  sem5=models.CharField(max_length=50)
  sem6=models.CharField(max_length=50)
  sem7=models.CharField(max_length=50)
  