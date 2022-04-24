from django.urls import path

from . import views

urlpatterns = [
   
   path('', views.home, name='home'),
   path('eventos', views.eventos, name='eventos'),
   path('eventos/<int:evento_id>', views.eventoDetalle, name='eventoDetalle'),
   path('quienesSomos', views.quienesSomos, name='quienesSomos'),
   path('padreLuisBernaola', views.padreLuisBernaola, name='padreLuisBernaola'),
   path('actividades', views.actividades, name='actividades'),
   path('libros', views.listaLibros, name='libros'),
   path('libro/<int:id_libro>', views.libroDetalle, name='libroDetalle'),
   path('libro/<int:id_libro>/autor/<int:id_autor>', views.autor, name='autor'),
   path('editorialDetalle/<int:id_editorial>', views.editorialDetalle, name='editorialDetalle'),
   path('socio', views.socio, name='socio'),
   path('patronato', views.patronato, name='patronato'),
   path('edicion', views.listaEdiciones, name='ediciones'),
   path('edicion/<int:id_beca>', views.edicionDetalle, name='edicionDetalle'),
   path('edicionPremios', views.edicionPremios, name='edicionPremios'),
   path('edicionPremios/<int:id_edicionPremios>', views.edicionPremioDetalle, name='edicionPremioDetalle'),
   path('contacto', views.formularioForm, name='contacto'),
   path('modulos', views.modulos, name='modulos'),
   path('modulos/<int:id_modulo>', views.moduloDetalle, name='moduloDetalle'),
   path('tedx', views.tedx, name='tedx'),
   path('seminarios', views.seminarios, name='seminarios'),
   path('seminarios/<int:id_modulo>', views.seminarioDetalle, name='seminarioDetalle'),
   path('patrocinio', views.patrocinio, name='patrocinio'),
   path('london', views.london, name='london'),
   path('legal', views.legal, name='legal'),
]

