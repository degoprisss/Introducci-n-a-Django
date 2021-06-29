
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from editorial.models import Editorial


class EditorialSerializer(ModelSerializer):

    class Meta:
        model = Editorial
        fields = ('nombre', 'email', 'pagina_web')

class CreateSerialaizar(ModelSerializer):

    class Meta:
        model = Editorial
        fields = ('nombre', 'email', 'pagina_web')


class SerializersPatchEditorial(ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('nombre', )

class EditorialSeriaizersViewSets(ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'