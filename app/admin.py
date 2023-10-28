from django.contrib import admin

from .models import adicionar

from .models import permisoes

from .models import datanumero

from .models import descri
# from .models import dadosdv
# Register your models here.


admin.site.register(adicionar)

admin.site.register(permisoes)

admin.site.register(datanumero)
# admin.site.register(dadosdv)
admin.site.register(descri)
