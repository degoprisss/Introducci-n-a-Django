
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from autor.models import Autor


class Autores(View):
    def get(self, request):
        data = Autor.objects.all()
        contexto = {'autores': data}
        print('metodo get')
        return render(request, 'autores/autores_listas.html', contexto)
    def post(self, request):
        createAutor = {
            'nombre': request.POST['nombre'],
            'email': request.POST['email'],
            'fecha_publicacion': request.POST['fecha_publicacion']
        }
        createExit = Autor.objects.create(**createAutor)

        if createExit:
            data = Autor.objects.all()
            contexto = {
                'autores': data,
                'mensaje': 'Todo salío bien!'
            }
        else:
            contexto = {}

        return render(request, 'autores/autores_listas.html', contexto)

class AutorDetalle(View):
    def get(self, request, autor_id):
        data = Autor.objects.filter(id=autor_id)
        return render(request, 'autores/autores_datalle.html', {'data': data})


