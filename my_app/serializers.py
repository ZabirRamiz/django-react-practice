from rest_framework import serializers
from .models import *

class MySerializer(serializers.ModelSerializer):

    class Meta:
        model = my_table
        fields = [
            'name',
            'age'
        ]