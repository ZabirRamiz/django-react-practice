from rest_framework import serializers
from .models import *

class somethingSerializer(serializers.ModelSerializer):
    class Meta():
        model = something
        fields = '__all__'

class whoSerializer(serializers.ModelSerializer):
    class Meta():
        model = who
        fields = '__all__'