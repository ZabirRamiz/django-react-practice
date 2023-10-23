from django.shortcuts import render

# to create the serializer
from .models import my_table
from .serializers import MySerializer
# to tell the api request
from rest_framework.decorators import api_view
# to generate json response
from django.http import JsonResponse

# Create your views here.



@api_view(["GET",'POST'])
def show_all(request):
    if request.method == "GET":
        
        query = 'select * from my_app_my_table'
        my_table_var = my_table.objects.raw(query)
        
        # my_table_var = my_table.objects.all()
        
        my_table_serializer = MySerializer(my_table_var, many = True)
        return JsonResponse(my_table_serializer.data, safe=False)
        
        


    elif request.method == "POST":
        query = "insert into my_app_my_table ('name','age') values (%s,%s)"

        my_table_var = my_table.objects.raw(query, [name,age])

