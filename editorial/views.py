#import permission as permission
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from editorial.models import Editorial
from editorial.serializers import EditorialSerializer, CreateSerialaizar, SerializersPatchEditorial


class EditorialGetPost(APIView):
    def get(self, request):
        editorialGet = Editorial.objects.all()
        serialaized = EditorialSerializer(editorialGet, many=True)
        return Response(data=serialaized.data)
    def post(self, request):
        serialized = CreateSerialaizar(data=request.data)
        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )

        serialized.save()
        return Response(status=status.HTTP_201_CREATED, data=serialized.data)


class EditorialGetPostGeneric(ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer



class EditorialViewSet(ModelViewSet):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    #permission_classes = (IsAuthenticated, )

    def get_permissions(self):
        if self.request.method == 'GET':
            permissions = (AllowAny, )
        else:
            permissions = (IsAuthenticated, )

        return [permission() for permission in permissions]


@api_view(['GET', 'POST'])
def getEditorial(request):
    if request.method == 'GET':
        editorialGet = Editorial.objects.all()
        serialaized = EditorialSerializer(editorialGet, many=True)
        return Response(data=serialaized.data)
    if request.method == 'POST':
        print(request.data)
        serialized = CreateSerialaizar(data=request.data)
        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )

        serialized.save()
    return Response(status=status.HTTP_201_CREATED, data=serialized.data)

@api_view(['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
def detalleEditorial(request, editorial_id):
    if request.method == 'PUT':
        editorial = Editorial.objects.get(id=editorial_id)
        serlializers = CreateSerialaizar(instance=editorial, data=request.data)

        if not serlializers.is_valid():
            return Response(status=status.HTTP_404_NOT_FOUND, data=serlializers.errors)

        serlializers.save()
        return Response(status=status.HTTP_200_OK, data=serlializers.data)

    if request.method == 'PATCH':
        editorial = Editorial.objects.get(id=editorial_id)
        serliazers = SerializersPatchEditorial(instance=editorial, data=request.data)

        if not  serliazers.is_valid():
            return Response(status=status.HTTP_404_NOT_FOUND, data=serliazers.errors)

        serliazers.save()
        return Response(status=status.HTTP_201_CREATED, data=serliazers.data)
    if request.method == 'DELETE':
        editorial = Editorial.objects.get(id=editorial_id)
        editorial.delete()

        return Response(status=status.HTTP_201_CREATED)