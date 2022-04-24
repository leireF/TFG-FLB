from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Cargo, Miembro, Socio, Autor, Editorial, Libro, Premio, Ganador, Jurado, EdicionPremio, Coordinador, Profesor
from .models import Tema, Modulo, ActividadFormacion, Evento, Beca, Beneficiario, EdicionBeca 

from .models import Mensaje
from .forms import FormularioForm

from django.http import HttpResponseRedirect

#SACA EL LISTADO DE LOS TRES ULTIMOS EVENTOS
def home(request):
	eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
	context = {'lista_eventos': eventos}
	return render(request, 'home.html', context)
    
#SACA EL LISTADO DE EVENTOS	
def eventos(request):
	eventos = get_list_or_404(Evento.objects.order_by('-fecha'))
	context = {'lista_eventos': eventos}
	return render(request, 'eventos.html', context) 

#SACA LOS DATOS CONCRETOS DE UNA NOTICIA	
def eventoDetalle(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    context = { 'evento': evento }
    return render(request, 'eventoDetalle.html', context) 

def quienesSomos(request):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    context = {'lista_eventos': eventos}
    return render(request, 'quienesSomos.html', context)   
	
def padreLuisBernaola(request):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    context = {'lista_eventos': eventos}
    return render(request, 'padreLuisBernaola.html', context)

def actividades(request):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    context = {'lista_eventos': eventos}
    return render(request, 'actividades.html', context)  	
        
#SACA EL LISTADO DE LIBROS
def listaLibros(request):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    libros = get_list_or_404(Libro.objects.order_by('titulo'))
    context = {'lista_libros': libros,'lista_eventos': eventos }
    return render(request, 'libros.html', context)  
  
#SACA LOS DATOS CONCRETOS DE UN LIBRO
def libroDetalle(request, id_libro):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    libro = get_object_or_404(Libro, pk = id_libro)
    autores = libro.autores.all()
    context = {'libro': libro, 'autores': autores,'lista_eventos': eventos}
    return render(request, 'libroDetalle.html', context)  

#SACA LOS DATOS CONCRETOS DE UN AUTOR
def autor(request, id_autor, id_libro):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    autor = get_object_or_404(Autor, pk = id_autor)
    libro = get_object_or_404(Libro, pk = id_libro)
    libros = autor.libro_set.all()
    context = {'libro': libro, 'autor' : autor ,'lista_libros': libros }
    return render(request, 'autor.html', context)

#SACA LOS LIBROS DE UNA EDITORIAL EN CONCRETO
def editorialDetalle(request, id_editorial):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    editorial = get_object_or_404(Editorial, pk = id_editorial)
    libros = editorial.libro_set.all()
    context = { 'editorial' : editorial ,'lista_libros': libros,'lista_eventos': eventos }
    return render(request, 'editorialDetalle.html', context)

#SACA EL LISTADO DE SOCIOS
def socio(request):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    #socioJuridico = get_list_or_404(Socio.objects.order_by('tipo').filter(tipo ='Persona Jurídica'))
    #socioFisico = get_list_or_404(Socio.objects.order_by('tipo').filter(tipo ='Persona Física'))
    #context = {'lista_socios_juridicos': socioJuridico, 'lista_socios_fisicos': socioFisico,'lista_eventos': eventos }
    context = {'lista_eventos': eventos}
    return render(request, 'socio.html', context)	
      
#SACA EL PATRONATO    
def patronato(request):
    cargos = get_list_or_404(Cargo.objects.order_by('cargo'))
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    context = {'cargos': cargos, 'lista_eventos': eventos}
    return render(request, 'patronato.html', context)
    
#SACA EL LISTADO DE EDICIONES DE BECAS
def listaEdiciones(request):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    #edicion = get_list_or_404(EdicionBeca.objects.order_by('-fecha'))
    #context = {'lista_ediciones': edicion, 'lista_eventos': eventos }
    context = {'lista_eventos': eventos }
    return render(request, 'ediciones.html', context)  
    
#SACA LOS DATOS CONCRETOS DE UNA EDICION
def edicionDetalle(request, id_beca):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    edicionBeca = get_object_or_404(EdicionBeca, pk = id_beca)
    beneficiario = edicionBeca.beneficiario.all()
    context = {'edicionBeca': edicionBeca, 'beneficiario' : beneficiario, 'lista_eventos': eventos}
    return render(request, 'edicionDetalle.html', context)  
	
#SACA EL LISTADO DE EDICIONES DE PREMIOS
def edicionPremios(request):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    #edicionPremios = get_list_or_404(EdicionPremio.objects.order_by('-fecha'))
    context = {'lista_eventos': eventos}
    #context = {'lista_edicionPremios': edicionPremios,'lista_eventos': eventos}
    return render(request, 'edicionpremio.html', context)  	

#SACA LOS DATOS CONCRETOS DE UNA EDICION
def edicionPremioDetalle(request, id_edicionPremios):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    edicionPremio = get_object_or_404(EdicionPremio, pk = id_edicionPremios)
    jurado = edicionPremio.jurado.all()
    context = {'edicionPremio': edicionPremio, 'jurado' : jurado,'lista_eventos': eventos}
    return render(request, 'edicionPremioDetalle.html', context)	
	
#SACA EL LISTADO DE CURSOS VARIOS
def modulos(request):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    cursosvarios = get_list_or_404(ActividadFormacion.objects.order_by('titulo').filter(tipo = 'Cursos Varios'))
    seminarios = get_list_or_404(ActividadFormacion.objects.order_by('titulo').filter(tipo = 'Seminarios'))
    context = {'lista_cursos': cursosvarios,'lista_seminarios': seminarios,'lista_eventos': eventos}
    return render(request, 'modulos.html', context)  	

#SACA LOS DATOS CONCRETOS DE UN CURSO
def moduloDetalle(request, id_modulo):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    modulo = get_object_or_404(Modulo, pk = id_modulo)
    coordinador = modulo.coordinadores.all()
    profesor = modulo.profesor.all()
    tema = modulo.tema.all()
    context = {'modulo': modulo, 'coordinador' : coordinador, 'profesor': profesor, 'tema': tema, 'lista_eventos': eventos}
    return render(request, 'moduloDetalle.html', context) 
    
#SACA LOS DATOS CONCRETOS DE UN SEMINARIO
def seminarioDetalle(request, id_modulo):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    modulo = get_object_or_404(Modulo, pk = id_modulo)
    coordinador = modulo.coordinadores.all()
    profesor = modulo.profesor.all()
    tema = modulo.tema.all()
    context = {'modulo': modulo, 'coordinador' : coordinador, 'profesor': profesor, 'tema': tema, 'lista_eventos': eventos}
    return render(request, 'seminarioDetalle.html', context)       
  
#SACA EL LISTADO DE SEMINARIOS
def seminarios(request):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    seminario = get_list_or_404(Evento.objects.order_by('tipo').filter(tipo ='Seminarios de apoyo en matemáticas y mat. financieras'))
    context = {'lista_seminario': seminario,'lista_eventos': eventos}
    return render(request, 'seminarios.html', context)     
  
#SACA LOS DATOS DEL EVENTO TEDX  
def tedx(request):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    tedx = get_list_or_404(Evento.objects.order_by('tipo').filter(tipo ='Tedx'))
    context = {'lista_tedx': tedx,'lista_eventos': eventos}
    return render(request, 'tedx.html', context)  
  
#SACA LOS DATOS DEL EVENTO PATROCINIO TRABAJOS INVESTIGACION  
def patrocinio(request):
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    patrocinio = get_list_or_404(Evento.objects.order_by('tipo').filter(tipo ='Patrocinio Trabajos Investigación'))
    context = {'lista_patrocinio': patrocinio,'lista_eventos': eventos}
    return render(request, 'patrocinio.html', context)  
  
#SACA LOS DATOS DEL EVENTO LONDON FINANCE SEMINAR  
def london(request):
    london = get_list_or_404(Evento.objects.order_by('tipo').filter(tipo ='London Finance Seminar'))
    eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
    context = {'lista_london': london,'lista_eventos': eventos}
    return render(request, 'london.html', context)  
    
def formularioForm(request):
	submitted = False
	if request.method == 'GET':
		form = FormularioForm(request.GET)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('contacto')
	else:        
		form = FormularioForm()
		
	if 'submitted' in request.GET:
		submitted = True
		
	return render(request, 'contacto.html', {'form':form})

#SACA LA INFORMACIÓN LEGAL DE PROTECCION DE DATOS
def legal(request):
	eventos = get_list_or_404(Evento.objects.order_by('-fecha')[:3])
	context = {'lista_eventos': eventos}
	return render(request, 'legal.html', context)
