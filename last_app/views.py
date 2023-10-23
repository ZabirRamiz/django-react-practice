from django.shortcuts import render
from rest_framework import response, viewsets
from .models import *
from .serializers import somethingSerializer,whoSerializer
from django.http import HttpResponse



# Create your views here.

class somethingViewset(viewsets.ModelViewSet):
    queryset = something.objects.all()
    serializer_class = somethingSerializer

class whoViewset(viewsets.ViewSet):
    queryset = who.objects.all()
    serializer_class = whoSerializer

def nothing(request):
    return HttpResponse("hello")