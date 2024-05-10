### L4Entrega2

Este es un proyecto paso a paso para crear un sitio web básico utilizando Django. A continuación se detallan los 21 pasos necesarios:

#### Paso 1: Instalar entorno virtual
```bash
python -m venv venv
```

#### Paso 2: Activar entorno virtual
```bash
venv\Scripts\activate
```

#### Paso 3: Instalar Django
```bash
pip install django
```

#### Paso 4: Crear proyecto
```bash
django-admin startproject web
```

#### Paso 5: Crear y configurar aplicaciones
```bash
#cd web
python manage.py startapp blog
python manage.py startapp nosotros
python manage.py startapp contacto
```

#### Paso 6: Agregar las aplicaciones a `settings.py`
```python
INSTALLED_APPS = [
    ...
    'home',
    'about',
    'contact',
]
```

#### Paso 7: Configurar las URL
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
]
```

#### Paso 8: Crear las vistas para cada aplicación
```python
# En home/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

# En about/views.py
from django.shortcuts import render

def about(request):
    return render(request, 'about/about.html')

# En contact/views.py
from django.shortcuts import render

def contact(request):
    if request.method == 'POST':
        # Procesar el formulario aquí y guardar la información en la base de datos si es necesario
        pass
    return render(request, 'contact/contact.html')
```

#### Paso 9: Crear los archivos HTML para cada aplicación
```
web/
├── home/
│   └── templates/
│       └── home/
│           └── home.html
├── about/
│   └── templates/
│       └── about/
│           └── about.html
└── contact/
    └── templates/
        └── contact/
            └── contact.html
```

#### Paso 10: Crear el formulario en la aplicación `contact`
```python
# En contact/forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensaje', widget=forms.Textarea)
```

#### Paso 11: Crear el contenido para cada archivo HTML
```html
<!-- En home/templates/home/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Principal</title>
</head>
<body>
    <h1>Bienvenido a nuestro sitio web</h1>
    <p>Texto introductorio...</p>
    <a href="{% url 'about' %}">Sobre Nosotros</a>
    <a href="{% url 'contact' %}">Contactanos</a>
    <!-- Agrega enlaces a las redes sociales aquí -->
</body>
</html>
```

#### Paso 12: Crear los archivos `urls.py` para cada aplicación
```python
# En home/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

#### Paso 13: Completar el archivo `views.py` de la aplicación `contact`
```python
# En contact/views.py
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage 

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['message']
            
            nuevo_mensaje = ContactMessage(nombre=nombre, email=email, mensaje=mensaje)
            nuevo_mensaje.save()
            
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

def success(request):
    return render(request, 'contact/success.html')
```

#### Paso 14: Crear el modelo en `models.py` de la aplicación `contact`
```python
# En contact/models.py
from django.db import models

class ContactMessage(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
```

#### Paso 15: Crear un archivo `success.html` para informar al usuario que el formulario fue enviado con éxito
```html
<!-- En contact/templates/contact/success.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario Enviado con Éxito</title>
</head>
<body>
    <h1>¡Formulario Enviado con Éxito!</h1>
    <p>¡Gracias por contactarnos! Nos pondremos en contacto contigo lo antes posible.</p>
</body>
</html>
```

#### Paso 16: Agregar estilos CSS a nuestros archivos HTML
```
mi_proyecto/
├── home/
│   ├── static/
│   │   └── css/
│   │       └── styles.css
├── about/
│   ├── static/
│   │   └── css/
│   │       └── styles.css
└── contact/
    ├── static/
    │   └── css/
    │       └── styles.css
```

#### Paso 17: Modificar el archivo `settings.py` para agregar los templates y los statics
```python
# En settings.py
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / "templates",],
    }
]

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```

#### Paso 18: Agregar el código Django `{% load static %}` en la primera línea de cada archivo HTML
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Principal</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
```

#### Paso 19: Crear las migraciones y migrar la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```



#### Paso 20: Crear el archivo `.gitignore` para evitar subir el entorno virtual a Git
venv/


#### Paso 21: Crear el archivo `requirements.txt` para guardar las dependencias de nuestro proyecto
```bash
pip freeze > requirements.txt
```

Sigue estos pasos para configurar tu proyecto y desarrollar un sitio web funcional utilizando Django. Si tienes alguna pregunta, ¡no dudes en preguntar!
