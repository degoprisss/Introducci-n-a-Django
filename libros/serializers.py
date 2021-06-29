from rest_framework.serializers import ModelSerializer

from libros.models import Libros


class LibrosSerializers(ModelSerializer):

    class Meta:
        model = Libros
        fields = ("nombre", "paginas")
        #fields = '__all__'


class SerlializersCreateLibros(ModelSerializer):

    class Meta:
        model = Libros
        fields = '__all__'
