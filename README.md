Pagina Web Fundación Luis Bernaola
===============================

Configuración
-------------

**PASO 1: Instala Django en un entorno virtual**

El primer paso será crear un entorno virtual y así disponer de un entorno aislado donde instalar nuestras dependencias de Django sin que nos afecten otras que tengamos instaladas en nuestro sistema. Para crear el entorno virtual:

    mkvirtualenv webflb

Activar el entorno (se activa automáticamente al crearlo)

    workon webflb

Podemos saber si estamos dentro de un entorno virtual porque la consola nos pondrá en toto momento el nombre del entorno en el que nos encontramos entre paréntesis. En este caso:

    (webflb) C:\Users\developer>

Recuerda que podemos saber las dependencias que tenemos instaladas en un entorno virtual ejecutando el comando `pip freeze`. Si lo hacemos ahora, no mostrará nada ya que acabamos de crear el entorno.

Por lo tanto, ahora toca instalar Django:

  pip install django

Si ejecutas el comando`pip freeze` una vez instalado Django, verás cómo muestra varias dependecias que ha instalado (aparecerá Django y otras dependencias que Django necesita):

    (empresaDjangoEnv) C:\Users\developer>pip freeze
    asgiref==3.5.0
    Django==4.0.3
    sqlparse==0.4.2
    tzdata==2022.1

Si tienes dudas sobre el uso de virtualenvwrapper y su configuración en PyCharm o Visual Studio Code, [puedes ver este video](https://youtu.be/lJrs7P9eKXc) donde se explica todo lo que necesitas saber.

**PASO 2: Crea tu primer proyecto**

Crea el proyecto Django:

  django-admin startproject TFGflb

La estructura de ficheros resultante es la siguiente:

    ```
    project/
        manage.py
        project/
        __init__.py
        settings.py
        urls.py
        wsgi.py

    ```

Inicia el servidor con el comando `python manage.py runserver` dentro del directorio del proyecto.

**PASO 3: Crea tu primera aplicación**

Posicionate en el directorio del proyecto `$ cd <project_folder>`

Crea la aplicación ejecutando el siguiente comando:

    python manage.py startapp appFLB

Dentro del directorio de la aplicación, crear un fichero llamado `urls.py` que utilizaremos para mapear las URLs de nuestra aplicación.
La estructura de ficheros resultante será la siguiente:

 project/
     manage.py
     db.sqlite3
     project/
 	__init__.py
 	settings.py
 	urls.py
 	wsgi.py
     app/
 	migrations/
 	    __init__.py
 	__init__.py
 	admin.py
 	apps.py
 	models.py
 	tests.py
 	urls.py
 	views.py

Incluir a aplicación dentro del fichero `settings.py` del proyecto, añadiendo el nombre a la lista `INSTALLED_APPS`:
	
	 INSTALLED_APPS = [
	 	'appFLB',
	 	# ...
	 ]

**PASO 4: Crea una nueva vista y configura su ruta de acceso**

Dentro del directorio de la app, abrir `views.py` y añadir lo siguiente:

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Listado de departamentos")
```
    
Crear el archivo `urls.py` dentro de la carpeta de la aplicación y añadir el patrón para la siguiente ruta:
   ```python
from django.urls import path
from . import views
   
urlpatterns = [
    path('', views.index, name='index'),
]
   ```
Con esto le estaremos diciendo que la función `index()` recién creada será la encargada de responder a las llamadas a esa ruta.

Como Django nos permite tener múltiples aplicaciones dentro de un proyecto, vamos a decirle qué ruta seguirán las llamadas a la aplicación `appFLB`. Para ello, dentro del directorio del proyecto hay que editar el archivo `urls.py` e incluir la redirección al fichero `urls.py` de la aplicación `appFLB`. El resultado debe ser el siguiente (no olvides importar la librería `include` de `django.urls`):

   ```python
from django.contrib import admin
from django.urls import include, path
  
urlpatterns = [
    path('appFLB/', include('appFLB.urls')),
    path('admin/', admin.site.urls),
]
   ```

En resumen, la idea es que cada aplicación gestiones sus rutas con su propio `urls.py` y en el `urls.py` del proyecto simplemente enlazarlos. En el ejemplo anterior, todas las rutas que vayan a `/appFLB` se gestionarán desde el urls.py que hemos creado.

Para comprobar que la vista funciona perfectamente, prueba a iniciar el servidor y acceder a la ruta: http://127.0.0.1:8000/appFLB/

**Enlace de la documenatcion en Internet**

    https://github.com/leireF/TFG-FLB.git

**Enlaces configuración Django**

    https://docs.djangoproject.com/en/4.0/howto/deployment/
    https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
