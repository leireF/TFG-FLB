from django.contrib import admin
from .models import Cargo, Miembro, Socio, Autor, Editorial, Libro, Premio, Ganador, Jurado, EdicionPremio, Coordinador, Profesor
from .models import Tema, Modulo, ActividadFormacion, Evento, Beca, EdicionBeca, Beneficiario

# Register your models here.
admin.site.register(Cargo)
admin.site.register(Miembro)
admin.site.register(Socio)
admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Premio)
admin.site.register(Ganador)
admin.site.register(Jurado)
admin.site.register(EdicionPremio)
admin.site.register(Coordinador)
admin.site.register(Profesor)
admin.site.register(Tema)
admin.site.register(Modulo)
admin.site.register(ActividadFormacion)
admin.site.register(Evento)
admin.site.register(Beca)
admin.site.register(EdicionBeca)
admin.site.register(Beneficiario)