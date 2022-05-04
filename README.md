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

Recuerda que podemos saber las dependencias que tenemos instaladas en un entorno virtual ejecutando el comando pip freeze. Si lo hacemos ahora, no mostrará nada ya que acabamos de crear el entorno.

Por lo tanto, ahora toca instalar Django:

  pip install django

Si ejecutas el comando pip freeze una vez instalado Django, verás cómo muestra varias dependecias que ha instalado (aparecerá Django y otras dependencias que Django necesita):

    (empresaDjangoEnv) C:\Users\developer>pip freeze
    asgiref==3.5.0
    Django==4.0.3
    sqlparse==0.4.2
    tzdata==2022.1

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

Inicia el servidor con el comando python manage.py runserver dentro del directorio del proyecto.

**PASO 3: Crea tu primera aplicación**

Posicionate en el directorio del proyecto $ cd <project_folder>

Crea la aplicación ejecutando el siguiente comando:

    python manage.py startapp appEmpresaDjango

Dentro del directorio de la aplicación, crear un fichero llamado urls.py que utilizaremos para mapear las URLs de nuestra aplicación.

**Enlace de la documenatcion en Internet**

    https://github.com/leireF/TFG-FLB.git

**Enlaces configuración Django**

    https://docs.djangoproject.com/en/4.0/howto/deployment/
    https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
