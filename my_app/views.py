from django.shortcuts import render

# to create the serializer
from .models import my_table
from .serializers import MySerializer
# to tell the api request
from rest_framework.decorators import api_view
from rest_framework.response import Response
# to generate json response
from django.http import JsonResponse

# Create your views here.
from django.db import connection


@api_view(["GET",'POST'])
def show_all(request):
    if request.method == "GET":
        query = 'select * from my_app_my_table'
        with connection.cursor() as cursor:
            cursor.execute(query)
            my_table_var = cursor.fetchall()
        print(my_table_var)
        lis = []
        for rows in my_table_var:
            out = {
                "id": rows[0],
                'name': rows[1],
                'age': rows[2]
            }
            lis.append(out) 
        return JsonResponse(lis, safe = False)

        # query = 'select * from my_app_my_table'
        # my_table_var = my_table.objects.raw(query)
        
        # my_table_var = my_table.objects.all()
        
        # my_table_serializer = MySerializer(my_table_var, many = True)
        # return JsonResponse(my_table_serializer.data, safe=False)
        
        


    elif request.method == "POST":
        query = "insert into my_app_my_table ('name','age') values (%s,%s)"

        my_table_var = my_table.objects.raw(query, [name,age])

