from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from libros.models import Libros
from libros.serializers import LibrosSerializers, SerlializersCreateLibros


class LibrosModelViewSet(ModelViewSet):
    queryset = Libros.objects.all()
    serializer_class = SerlializersCreateLibros

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LibrosSerializers

        return SerlializersCreateLibros


@api_view(['GET', 'POST'])
def getLibros(request):
    if request.method == 'GET':
        libros = Libros.objects.all()
        serializersLibros = LibrosSerializers(libros, many=True)
        return Response(data=serializersLibros.data)

    if request.method == 'POST':
        serializerPost = SerlializersCreateLibros(data=request.data)
        if not serializerPost.is_valid():
            return Response(status=status.HTTP_404_NOT_FOUND, data=serializerPost.errors)

        serializerPost.save()
        return Response(status=status.HTTP_201_CREATED, data=serializerPost.data)

