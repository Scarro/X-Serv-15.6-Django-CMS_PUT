from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Pages


def index(request):
    template = 'cms/index.html'
    context = {
        'pages': Pages.objects.all()
    }
    return render(request, template, context)

@csrf_exempt
def recurso(request, nombre):
    if request.method == "GET":
        # Obtengo la entrada agregada al diccionario o devuelvo un error
        recurso = get_object_or_404(Pages, nombre=nombre);
        template = 'cms/recurso.html'
        context = {
            'recurso': recurso
        }
    if request.method == "PUT":
        try:
            recurso = Pages.objects.get(nombre=nombre)
            template = 'cms/recurso.html'
            context = {
                'recurso': recurso
            }
        except (KeyError, Pages.DoesNotExist):
            recurso = request.body
            print recurso
            nuevo = Pages.objects.create(nombre=nombre, recurso=recurso)
#            Pages.object.create(nombre=nombre, recurso=recurso)
            template = 'cms/recursonuevo.html'
            context = {
                'recurso': nuevo
            }
    return render(request, template, context)