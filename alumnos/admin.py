from django.contrib import admin
from .models import Alumno, Genero

# Register your models here.
admin.site.register(Genero)
admin.site.register(Alumno)


