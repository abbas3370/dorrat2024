from django.urls import  path
from . import views

urlpatterns=[
    path('note',views.note001,name='note'),
    path('note1',views.note1,name='note1'),
    path('note005',views.name001,name='note005'),
    path('note003',views.photo001,name='صور'),
    path('مستخدم',views.form001,name='form1'),
]