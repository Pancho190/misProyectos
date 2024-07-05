from django.shortcuts import render

from .models import Alumno,Genero
# Create your views here.

def index(request):
    alumnos= Alumno.objects.all()
    context={}
    return render(request, 'alumnos/index.html', context)

def listadoSQL(request):
    alumnos= Alumno.objects.raw('SELECT * FROM alumnos_alumno')
    print(alumnos)
    context={"alumnos":alumnos}
    return render(request, 'alumnos/listadoSQL.html', context)

def crud(request):
    alumnos = Alumno.objects.all()
    context = {'alumnos': alumnos}
    return render(request, 'alumnos/alumnos_list.html', context)

def alumnosAdd(request):
    if  request.method is not "POST":
        
        generos=Genero.objects.all()
        context={'generos':generos}
        return render(request, 'alumnos/alumnos_add.html', context)
    else:

        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono = request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        active="1"

        objGenero=Genero.objects.get(id_genero = genero)
        obj=Alumno.objects.create( rut=rut, 
                                   nombre=nombre,
                                   apellido_paterno=aPaterno,
                                   apellido_materno=aMaterno,
                                   fecha_nacimiento=fechaNac,
                                   id_genero=objGenero,
                                   telefono=telefono,
                                   email=email,
                                   direccion=direccion,
                                   activo=1 )
        obj.save() 
        context={'mensaje':'Ok, datos grabados...'}
        return render(request, 'alumnos/alumnos_add.html', context)
    

def alumnos_del(request,pk):
    context={}
    try:
        alumno=Alumno.objects.get(rut=pk)

        alumno.delete()
        mensaje="Bien, datos eliminados"
        alumnos = Alumno.objects.all()
        context ={'alumnos':alumnos, 'mensaje':mensaje}
        return render(request, 'alumnos/alumnos_list.html', context)
    except:
        mensaje = "Error, rut no existe"
        alumnos = Alumno.objects.all()
        context={'alumnos':alumnos,'mensaje':mensaje}
        return render(request,'alumnos/alumnos_list.html',context)


def alumnos_findEdit(request,pk):

    if pk !="":
        alumno= Alumno.objects.get(rut=pk)
        generos=Genero.objects.all()

        print(type(alumno.id_genero.genero))

        context={'alumno':alumno,'genero':generos}
        if alumno:
            return render(request,'alumnos/alumnos_edit.html',context)
        else:
            context={'mensaje':"Error, rut no existe"}
            return render(request,'alumnos/alumnos_list.html',context)
        

def alumnosUpdate(request):
    if request.method== 'post':
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objectGenero=Genero.objects.get(id_genero = genero)

        alumno = Alumno()
        alumno.rut = rut
        alumno.nombre= nombre
        alumno.apellido_paterno=aPaterno
        alumno.apellido_materno = aMaterno
        alumno.fecha_nacimiento = fechaNac
        alumno.id_genero=objectGenero
        alumno.telefono=telefono
        alumno.email=email
        alumno.direccion=direccion
        alumno.activo=1
        alumno.save()

        generos=Genero.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'genero':generos,'alumno':alumno}
        return render(request,'alumnos/alumnos_edit.html', context)
    else:
        alumnos=Alumno.objects.all()
        context={'alumnos':alumnos}
        return render(request,'alumnos/alumnos_list.html',context)

def crud_generos(request):

    generos=Genero.objects.all()
    context ={'generos':generos}
    print("enviando datos generos_list")
    return render(request,"alumnos/generos_list.html",context)
