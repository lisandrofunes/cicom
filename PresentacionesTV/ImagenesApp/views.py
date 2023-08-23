from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Archivo, DetallePresentacion, Presentacion
from django.views import View
from django.http import HttpResponse
from django.views.generic.edit import CreateView

# class CargarArchivoView(View):
# def post(self, request):
#         nombre = request.POST.get('nombre')
#         archivo = request.FILES.get('archivo')  # Obtener el archivo de la solicitud POST

#         nuevo_archivo = Archivo(nombre=nombre, archivo=archivo)
#         nuevo_archivo.save()

#         return HttpResponse("Archivo cargado exitosamente")

class CargarArchivoView(View):
    def post(self, request):
        nombre = request.POST.get('nombre')
        archivo = request.FILES.get('archivo')  # Obtener el archivo de la solicitud POST

        nuevo_archivo = Archivo(nombre=nombre, archivo=archivo)
        nuevo_archivo.save()

        return HttpResponse("Archivo cargado exitosamente")

    def get(self, request):
        return render(request, 'cargar_archivo.html')




class ArchivoCreate(CreateView):
    model = Archivo
    # permission_required = 'catalog.can_mark_returned'
    fields = '__all__'
    template_name =  'ImagenesApp/archivo_form.html'
    success_url = reverse_lazy('index')



from django.shortcuts import render

def index(request):
    return render(request, 'ImagenesApp/index.html')




def crear_presentacion(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        archivo_ids = request.POST.getlist('archivos')  # Obtener una lista de IDs de archivos seleccionados

        nueva_presentacion = Presentacion(titulo=titulo)
        nueva_presentacion.save()

        for index, archivo_id in enumerate(archivo_ids):
            archivo = Archivo.objects.get(pk=archivo_id)
            DetallePresentacion.objects.create(presentacion=nueva_presentacion, archivo=archivo, orden=index)

    # Resto de tu vista...

from django.views import generic
class ArchivoListView(generic.ListView):
    model = Archivo
 