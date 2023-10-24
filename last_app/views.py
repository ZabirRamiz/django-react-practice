from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import response, viewsets
from .models import *
from .serializers import somethingSerializer,whoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



# Create your views here.

class somethingViewset(viewsets.ModelViewSet):
    queryset = something.objects.all()
    serializer_class = somethingSerializer

class whoViewset(viewsets.ViewSet):
    queryset = who.objects.all()
    serializer_class = whoSerializer


@api_view(["POST"])
def nothing(request):
    # if request.method() == "GET":
    # query = 'select noone, someone from last_app_something where noone = %s, someone= %s', [request.data['noone'],request.data['someone']]
    # nothing = something.objects.raw(query)
    nothing =  something.objects.filter(noone = request.data['noone'], someone=request.data['someone'])
    serializer = somethingSerializer(nothing, many = True)

    # return JsonResponse(serializer.data)
    return Response(serializer.data)