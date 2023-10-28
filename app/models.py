from django.db import models

# Create your models here.



    
class permisoes(models.Model):

    id = models.AutoField(primary_key=True)
    
    chavep = models.TextField(max_length=13)

    nomeunico = models.TextField(max_length=20)

    numeros = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nomeunico


class adicionar(models.Model):


    dicionar = models.TextField(max_length=20)
   
    def __str__(self) -> str:

        return self.dicionar


class datanumero(models.Model):
      d = models.TextField(max_length=10)
      n = models.IntegerField()
      video = models.TextField(max_length=100)

      def __str__(self) -> str:

        return self.d



class naorepeti(models.Model):

    recebenumero = models.TextField(max_length=20)
    
    def __str__(self) -> str:

        return self.recebenumero
    

class descri(models.Model):

   escrevadescricao = models.TextField(max_length=5000)
   def __str__(self) -> str:

        return self.escrevadescricao