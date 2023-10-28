from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import permisoes
from django.db.models import Q
from app.models import adicionar
from app.models import datanumero
from app.models import naorepeti
from app.models import descri
import time
import os
import re
# Create your views here.
  # background-image: url({% static 'pp.webp'%});
  #        background-repeat: no-repeat;
  #        background-size:cover;

def index(request):
    
    if request.method == 'GET':
     nus = request.COOKIES.get('seunumero')
    
     f = {
         'mostraa': permisoes.objects.all(),
         'ad': adicionar.objects.all(),
         'ch': datanumero.objects.all(),
         'sr':nus,
       
          
     }
   
     res = render(request,'fra.html',f)
    #  res.set_cookie('videos',50,99999)

     i = request.COOKIES.get('videos')
  
     return res
    else:
       a = permisoes()
       a.chavep = request.POST.get('num')
       a.nomeunico = request.POST.get('nome')
       a.numeros = request.POST.get('numero')
       numero001 =  request.POST.get('numero')
       m = request.POST.get('numero')
       llx = int(m)
       if llx <= 9999:
           
       #g =  request.POST.get('nome')
         naorepeti = permisoes.objects.filter(numeros__exact=numero001)
       
         if naorepeti:
            xx = 'Escolhar outro numero esse ja foi escolhido!'
            kx = {
           'ty':xx,
           'ks': permisoes.objects.all(),
           'mostraa': permisoes.objects.all(),
           'ad': adicionar.objects.all(),
           'ch': datanumero.objects.filter(id=1),
            }

            return render(request,'fra.html',kx)

         ui = "Cadastrado(a) com sucesso."
         
         
         m3 = request.POST.get('numero')
         
         

         jj = {
           'h':ui,
           'mostraa': permisoes.objects.all(),
           'ad': adicionar.objects.all(),
           'ch': datanumero.objects.filter(id=1),
         }

        
         res2 = render(request,'fra.html',jj)
       
        
         tra = str(m3)
         verificar = request.COOKIES.get('acesso22')
         if verificar != '10':
            a.save()
            res2.set_cookie('acesso22',10,999999)

            res2.set_cookie('seunumero',tra,999999)
           
         else:
             print('ja exit')

        
         return res2
    #    return HttpResponse('deu certo')
       else:
          xc = "Numero max -9999"
          
          xu = {
           'hx':xc,
           'mostraa': permisoes.objects.all(),
           'ad': adicionar.objects.all(),
           'ch': datanumero.objects.filter(id=1),
         }

          return render(request,'fra.html',xu)
           
 
      

def mostra(request):
    
     
      pega = request.POST.get('pes') 

      yy = {
          'oooo':permisoes.objects.filter(numeros__exact=pega),
      }

      return render(request,'t.html',yy)
       


def dd(request):
   
   dx = {
      'lg':descri.objects.all(),
   }


   return render(request,'d.html',dx)