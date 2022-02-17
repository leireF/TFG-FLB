from django.db import models
from django.forms import ModelForm
from datetime import datetime

#https://github.com/jvadillo/curso-django-paso-a-paso
		
class Miembro(models.Model):
    #id = models.AutoField(primary_key=True)
    fechaComienzo = models.DateField(null=True,blank=True)
    fechaFin = models.DateField(null=True,blank=True) # PONIENDO BLANK=TRUE se soluciona lo de que las fechas no sean obligatorias
    nombre = models.CharField(max_length= 20, default=" ")
    apellido = models.CharField(max_length= 30, default=" ")
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    
    def get_absolute_url(self):
        return reverse("miembro-detalle", kwargs={"pk": self.id}) 
		
    def __str__(self):
        return self.nombre
        
class Cargo(models.Model):
    #id = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length= 30, default=" ")
    miembro = models.ManyToManyField(Miembro)
	
    def get_absolute_url(self):
        return reverse("cargo-detalle", kwargs={"pk": self.id}) 
		
    def __str__(self):
        return self.cargo
        
TIPOS_SOCIOS = (
    ('Persona Jurídica','persona jurídica'),
    ('Persona Física','persona física'),
)
    
class Socio(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length= 40, default=" ")
    apellido = models.CharField(max_length = 30, default="", blank=True)
    NIF = models.CharField(max_length= 20, default="", blank=True)
    tipo = models.CharField(max_length=30, choices=TIPOS_SOCIOS)
    fecha_alta = models.DateField(null=True,blank=True)
    fecha_baja = models.DateField(null=True,blank=True)
    
    def get_absolute_url(self):
        return reverse("socio-detalle", kwargs={"pk": self.id}) 
		
    def __str__(self):
        return self.nombre
        
class Autor(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default="")
    apellido = models.CharField(max_length = 30, default="")
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    
    def get_absolute_url(self):
        return reverse("autor-detalle", kwargs={"pk": self.id})
		
    def __str__(self):
        return self.nombre
   
class Editorial(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default="")
   
    def get_absolute_url(self):
        return reverse("editorial-detalle", kwargs={"pk": self.id})
		
    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    #id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, default="")
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    sinopsis = models.CharField(max_length=2000, default="", blank=True)
    fecha_publicacion = models.DateField(null=True,blank=True)
    autores = models.ManyToManyField(Autor)
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image') #RUTA BUENA DE IMAGENES. para que funcione despues de subirlas copiar la carpeta y meterla dentro de appFLB\STATIC
    url = models.URLField(null=True, blank=True, verbose_name="Dirección Web")
     
    def get_absolute_url(self):
        return reverse("libro-detalle", kwargs={"pk": self.id}) 
		
    def __str__(self):
        return self.titulo
        
class Premio(models.Model):
    #id = models.AutoField(primary_key=True)
    introduccion = models.CharField(max_length= 1000, default="", blank=True)
    objetivo = models.CharField(max_length= 1000, default="", blank=True)
    dirigido = models.CharField(max_length= 1000, default="", blank=True)
    premio = models.CharField(max_length=50, default="")
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    url = models.URLField(null=True, blank=True, verbose_name="Dirección Web")
    
    def get_absolute_url(self):
        return reverse("premio-detalle", kwargs={"pk": self.id})
		
    def __str__(self):
        return self.premio
        
class Ganador(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default="")
    apellido = models.CharField(max_length=50, default="")
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    
    def get_absolute_url(self):
        return reverse("ganador-detalle", kwargs={"pk": self.id})
		
    def __str__(self):
        return self.nombre   
        
class Jurado(models.Model):
    #id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, default="")
    apellido = models.CharField(max_length=50, default="")
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    
    def get_absolute_url(self):
        return reverse("jurado-detalle", kwargs={"pk": self.id})
		
    def __str__(self):
        return self.nombre 
        
class EdicionPremio(models.Model):
    #id = models.AutoField(primary_key = True)
    fecha = models.DateField(null=True,blank=True)
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    edicionPremio = models.CharField(max_length=20, default="")
    premio = models.ForeignKey(Premio, on_delete=models.CASCADE) 
    ganador = models.ForeignKey(Ganador, on_delete=models.CASCADE) 
    jurado = models.ManyToManyField(Jurado)

    def get_absolute_url(self):
        return reverse("edicionPremio-detalle", kwargs={"pk": self.id})  
		
    def __str__(self):
        return self.edicionPremio
        
TIPOS_ACTIVIDADES = (  
    ('Cursos Varios','cursos varios'),
    ('Seminarios','seminarios'),
)

class Coordinador(models.Model):
    #id = models.AutoField(primary_key = True)
    cargo = models.CharField(max_length= 100, default="")
    texto = models.CharField(max_length=1000, default="")

    def get_absolute_url(self):
        return reverse("coordinadores-detalle", kwargs={"pk": self.id})
		
    def __str__(self):
        return self.texto  
        
class Profesor(models.Model):
    #id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=30, default="")
    apellidos = models.CharField(max_length=100, default="")
    cargo = models.CharField(max_length= 100, default="")

    def get_absolute_url(self):
        return reverse("profesor-detalle", kwargs={"pk": self.id})  
		
    def __str__(self):
        return self.nombre
        
class Tema(models.Model):
    #id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length= 100, default="", blank=True)
    parte = models.CharField(max_length = 100, default="", blank=True)
    programa = models.TextField(default="")

    def get_absolute_url(self):
        return reverse("tema-detalle", kwargs={"pk": self.id})    
		
    def __str__(self):
        return self.programa 
 
class Modulo(models.Model):
    #id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length= 50, default="")
    coordinadores = models.ManyToManyField(Coordinador)
    profesor = models.ManyToManyField(Profesor)
    tema = models.ManyToManyField(Tema)
    
    def get_absolute_url(self):
        return reverse("modulo-detalle", kwargs={"pk": self.id})
		
    def __str__(self):
        return self.titulo 
 
class ActividadFormacion(models.Model):
    #id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length= 50, default="")
    tipo = models.CharField(max_length=30, choices=TIPOS_ACTIVIDADES)
    modulos = models.ManyToManyField(Modulo)
    
    def get_absolute_url(self):
        return reverse("actividadFormacion-detalle", kwargs={"pk": self.id})
		
    def __str__(self):
        return self.titulo    
  
TIPOS_EVENTOS = (
    ('Tedx','tedx'),
    ('Patrocinio Trabajos Investigación','patrocinio trabajos investigación'),
	('London Finance Seminar','london finance seminar'),
)
	 
class Evento(models.Model):
    #id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, default="")
    fecha = models.DateField(null=True,blank=True)
    texto = models.CharField(max_length=1000, default="")
    tipo = models.CharField(max_length=50, choices=TIPOS_EVENTOS)
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    url = models.URLField(null=True, blank=True, verbose_name="Dirección Web")
    
    def get_absolute_url(self):
        return reverse("evento-detalle", kwargs={"pk": self.id})
		
    def __str__(self):
        return self.titulo   
        
class Beneficiario(models.Model):
    #id = models.AutoField(primary_key=True)
    empresa = models.CharField( max_length=100, default="")
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    
    def get_absolute_url(self):
        return reverse("beneficiario-detalle", kwargs={"pk": self.id})
		
    def __str__(self):
        return self.empresa   

class Beca(models.Model):
    #id = models.AutoField(primary_key=True)
    tipo = models.CharField( max_length=100, default="")
    duracion = models.CharField( max_length=100, default="")
    importe = models.DecimalField(max_digits = 5, decimal_places = 2)
    
    def get_absolute_url(self):
        return reverse("beca-detalle", kwargs={"pk": self.id})
		
    def __str__(self):
        return self.tipo 
 
class EdicionBeca(models.Model):
    #id = models.AutoField(primary_key = True)
    fecha = models.DateField(null=True,blank=True)
    beca = models.ForeignKey(Beca, on_delete=models.CASCADE)
    edicionBeca = models.CharField( max_length=20, default="")
    imagen = models.ImageField(upload_to='img',blank=True,null=True,verbose_name='Image')
    beneficiario = models.ManyToManyField(Beneficiario)
    
    def get_absolute_url(self):
        return reverse("edicionBeca-detalle", kwargs={"pk": self.id})
		
    def __str__(self):
        return self.edicionBeca       
        
class Mensaje(models.Model):
    #id = models.AutoField(primary_key=True)
    nombreApellidos = models.CharField( max_length=50, default="")
    dni = models.CharField(max_length=9, default="")
    telefono = models.IntegerField()
    email= models.EmailField( max_length=30, default="")
    texto = models.TextField(default="")
    
    def __str__(self):
        return self.nombreApellidos
