from rest_framework import serializers
from . import models

class MySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.my_table
        fields = [
            'name',
            'age'
        ]