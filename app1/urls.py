
from django.urls import path

from . import views

urlpatterns = [


    path('news',views.news,name='news'),
   
    path('app1/direct1',views.passdirect,name='index1001'),
    path('app1/direct',views.direct,name='index'),
    path('app1/maitre1',views.passmaitre,name='index199299'),
    path('app1/directmaitre',views.maitres,name='index'),
    path('app1/direct/directimage',views.insertimage,name='image001'),
    path('app1/direct/addimage1',views.addimage1,name='addimage001'),
    path('app1/direct/delimage1/<int:cc>',views.delimage1,name='delimage008'),
    
    path('app1/direct/directvideo',views.insertvideo,name='video001'),
    path('app1/direct/addvideo1',views.addvideo1,name='addvideo001'),
    path('app1/direct/delvideo1/<int:cc>',views.delvideo1,name='delivideo008'),
    
    ###    عرض الصور والفيديوهات للأهل
    path('app1/direct/directimagepare',views.insertimagepare,name='image001pare'),
    path('app1/direct/directvideopare',views.insertvideopare,name='video001pare'),
    ######
    
    path('الامتحانات',views.index,name='index'),
    path('الاعطال',views.about,name='about'),
    path('',views.bord,name='bord'),
    path('app1/photo',views.photo,name='photo'),
    path('النشرات',views.sendvar,name='variable'),
    path('app1/user',views.form0001,name='form01'),
    path('app1/user003',views.form0003,name='form03'),
    path('app1/matiere',views.form0004,name='form04'),
    path('app1/matiereedit',views.matiereupdate,name='form09'),
    path('app1/eleve/update',views.editstudent,name='form1001'),
    
    
    path('app1/eleve1/list',views.listeleve,name='form10033'),
    path('app1/eleve1/update1/<str:cod>',views.update1,name='update'),
    path('app1/eleve1/update1/updaterecord/<str:coood>',views.updaterecord,name='updaterecord'),
    path('app1/eleve1/add',views.addstudent,name='addeleve'),
    path('app1/eleve1/del/<str:cod01>',views.dele,name='deldeleve'),
    #############path('app1/eleve1/updateliste/<str:cod008>',views.updateliste,name='updlist'),


    path('app1/direct/list-m',views.listematiere,name='form10033m'),
    path('app1/direct/updatematiere/<str:cod>',views.updatematiere001,name='update001'), 
    path('app1/direct/updatematiere/updaterecordmatiere/<str:coood>',views.updaterecordmatiere,name='update003'), 
    path('app1/direct/addmatiere',views.addmatiere0024,name='add_0m'),
    path('app1/direct/del_m/<str:cod01>',views.dele_m,name='delmatiere'),
    path('app1/direct/autocodemat/<str:anmat>/<str:sec05>',views.autocodemat,name='codemat'),
    path('app1/direct/list-m/rescore/<int:nn1>',views.rescore,name='form10033score001'),

    

    path('app1/direct/list-anne',views.listanne,name='form10033anne'),
    path('app1/direct/updatanne/<str:cod>',views.updatanne,name='update001-a'), 
    path('app1/direct/updatanne/updaterecordanne/<str:coood>',views.updaterecordanne,name='updaterecord001'),
    path('app1/direct/addan',views.addanne,name='add_an'),
    path('app1/direct/dela/<str:cod01>',views.dela,name='delanne'),

    
    path('app1/direct/openaneleve1',views.openaneleve,name='openeleve'), 
    
    path('app1/direct/listenote1',views.listenote,name='listnote'), 
    
    path('app1/eleve1mat/listmat',views.listelevemat,name='form10033mat'),
    path('app1/eleve1mat/updateliste/<str:cod008>/<str:ann2002>',views.updateliste,name='form10033classc'),

    path('app1/eleve1notemaitre/listenotemaitre1',views.listenotemaitre,name='form10033note0012'),
    path('app1/eleve1notemaitre/updatenotemaitre/<str:code008>/<str:nomat>/<str:xw01>/<str:xw02>/<str:xw03>',views.updatenotemaitre,name='form10033classc0012'),

    path('app1/naitre1/listeusermaitre1',views.listeusermaitre,name='form100959'),
    path('app1/naitre1/delmaitreuser/<str:cod01>',views.delmaitreuser,name='delmaitreuser'),    
    path('app1/naitre1/updtusermaitre/<str:cod>',views.updtusermaitre,name='updatepr'),
    path('app1/naitre1/updtusermaitre/updaterecordusermaitre/<str:coood>',views.updaterecordusermaitre,name='updaterecordmaitre'),
    path('app1/naitre1/addusermaitre',views.addusermaitre,name='addusrmaitr'),
    
    
    path('app1/eleve1notedirect/listenotedirect',views.listenotedirect,name='form10033note0019'),
    path('app1/eleve1notedirect/updatenotedirect/<int:somtxx>/<int:idsa>/<str:codea1>/<str:anne2025>/<str:classe2025>/<str:section2025>/<str:month2025>',views.updatenotedirect,name='form10033classc0017'),


    path('app1/eleve1notedirect2030/regcarnet',views.regcarnet,name='form10033note20309'),

    path('app1/eleve1notedirect2035/rasmicarnet',views.rasmicarnet,name='form10033note2030559'),
     
    path('app1/eleve1notedirect/exportcarnets',views.exportcarnets,name='form10033notecarnet09'), 
    path('app1/elevecarnet/carnetuneleve',views.carnetuneleve,name='form10033carneteleve0030'), 

    path('app1/visa1/visamoyenne',views.visamoyenne,name='form10033vidsa'), 
    
   
   
    path('app1/mony/monylist',views.monylist,name='monyDL'),
    path('app1/mony/monyupdate/<int:idm>/<str:anne009>',views.monyupdate,name='monyDL005'),

    path('app1/eleves001/ifadah',views.ifadah,name='ifadah0033'),
    path('app1/eleves001/callmony/<str:x0>/<str:x1>/<str:x2>/<str:x3>/<str:x4>/<str:x6>/<str:x7>/<str:x8>',views.callmony,name='callmonyDL009'),
    path('app1/eleves001/callmonyt/<str:x0>/<str:x1>/<str:x2>/<str:x3>/<str:x4>/<str:x6>/<str:x7>/<str:x8>',views.callmonyt,name='callmonyDL009t'),
    path('app1/eleves001/callmonyz/<str:x0>/<str:x1>/<str:x2>/<str:x3>/<str:x4>/<str:x6>/<str:x7>/<str:x8>',views.callmonyz,name='callmonyDL009z'),
    path('app1/eleves001/callmonyd/<str:x001>/<str:x0>/<str:x1>/<str:x2>/<str:x3>/<str:x4>/<str:x6>/<str:x7>/<str:x8>',views.callmonyd,name='callmonyDL009'),
    path('app1/eleves001/callmonyG/<str:x0>/<str:x1>/<str:x2>/<str:x3>/<str:x4>/<str:x6>/<str:x7>/<str:x8>',views.callmonyG,name='callmonyGL009'),
    path('app1/eleves001/listaksat/<str:x6>/<str:x7>/<str:x8>',views.listaksat,name='callaksate'),
    path('app1/eleves001/callmonycha/<str:x0>/<str:x1>/<str:x2>/<str:x3>/<str:x4>/<str:x6>/<str:x7>/<str:x8>',views.callmonycha,name='callmonych007'),



###path('app1/naitre1/listeusermaitre1',views.listeusermaitre,name='form100959'),
   #### path('app1/naitre1/delmaitreuser/<str:cod01>',views.delmaitreuser,name='delmaitreuser'),    
    
    path('app1/school/updateschool',views.updateschool,name='form1school'),
    
#################################
#################################
#################  ps1 ps2 ps3

    path('app1/eleveps/listmatiereps123',views.listmatiereps123,name='formpsmatiere'),
    path('app1/eleveps/updatematps/<int:cod0035>/<str:s1>/<str:s2>/<str:s3>/<str:s4>/<str:s5>/<str:s6>/<int:s7>/<int:s8>/<str:ann01>/<str:class01>',views.updatematps,name='updpsmatiere'),

    path('app1/eleveps/addmatps',views.addmatps,name='addpsmatiere'),
    path('app1/eleveps/delps/<str:cod01>',views.delps,name='delpsmatiere'),
    
########################فتح عام دراسي للروضات

    path('app1/direct/openaps',views.openaps,name='openeleveps123'), 


# اصدار وادخال علامات الروضات من قبل المدير
    path('app1/directcarnetps/expcarnetps',views.expcarnetps,name='psnotedirect'),
    path('app1/directcarnetps/savenoteps/<int:cod>/<str:a>/<str:c>/<str:s>/<str:n>/<str:f0>',views.savenoteps,name='savenotepsdrct'),
# اصدار وادخال علامات الروضات من قبل الاستاذ 
    path('app1/Adirectcarnetps/Aexpcarnetps',views.Aexpcarnetps,name='Apsnotedirect'),
    path('app1/Adirectcarnetps/Asavenoteps/<int:cod>/<str:a>/<str:c>/<str:s>/<str:n>/<str:f0>',views.Asavenoteps,name='Asavenotepsdrct'),
   
    path('app1/FAdirectcarnetps/FAexpcarnetps',views.FAexpcarnetps,name='ApsnotedirectF'),
    path('app1/FAdirectcarnetps/FAsavenoteps/<int:cod>/<str:a>/<str:c>/<str:s>/<str:n>/<str:f0>',views.FAsavenoteps,name='AsavenotepsdrctF'),
# اظهار علامة تلميذ روضة محدد للاهل
    path('app1/parentcarnetps/expuncarnetps',views.expuncarnetps,name='psnoteparent'),



####   news

    path('app1/eleve1/listnews',views.listelevenews,name='form10033news'),
    path('app1/eleve1/updatelistenews/<int:cod>',views.updatelistenews,name='updatenews'),
########    path('app1/eleve1/update1/updaterecord/<str:coood>',views.updaterecord,name='updaterecord'),
    path('app1/eleve1/addnews',views.addnews,name='addnews'),
    path('app1/eleve1/delnews/<str:idd>',views.delnews,name='delnews'),




   
    ]
   
   
