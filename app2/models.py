from django.db import models

# Create your models here.


class student(models.Model):
  tuser =models.TextField()
  tpass= models.TextField()
  tname= models.TextField()
  tcountry= models.TextField()
  tmail =models.TextField()
  tphone=models.TextField()
  tclasse=models.TextField()
  tsection= models.TextField()
  timage =models.TextField()

class note(models.Model):
  user = models.TextField()
  name= models.TextField()
  classe= models.TextField()
  section = models.TextField()
  anne= models.TextField()
  month = models.TextField()
  math =models.DecimalField(max_digits=4 , decimal_places=2),
  physique =models.DecimalField(max_digits=4 , decimal_places=2) 
  chimie =models.DecimalField(max_digits=4 , decimal_places=2) 
  bio =models.DecimalField(max_digits=4 , decimal_places=2) 
  arab =models.DecimalField(max_digits=4 , decimal_places=2) 
  francais =models.DecimalField(max_digits=4 , decimal_places=2) 
  civisme=models.DecimalField(max_digits=4 , decimal_places=2) 
  historique =models.DecimalField(max_digits=4 , decimal_places=2) 
  geographie =models.DecimalField(max_digits=4 , decimal_places=2) 
  economie =models.DecimalField(max_digits=4 , decimal_places=2) 
  socialite =models.DecimalField(max_digits=4 , decimal_places=2) 
  philosophie =models.DecimalField(max_digits=4 , decimal_places=2) 
  informatique =models.DecimalField(max_digits=4 , decimal_places=2) 
  religieu =models.DecimalField(max_digits=4 , decimal_places=2)
  art =models.DecimalField(max_digits=4 , decimal_places=2) 
  pass1  =models.DecimalField(max_digits=4 , decimal_places=2)

### image=models.ImageField(upload_to='photos/%y/%m/%d)
### active=models.BooleanField(default=True)

