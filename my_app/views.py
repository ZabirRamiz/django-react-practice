from django.shortcuts import render


from .models import my_table
from .serializers import MySerializer

from django.http import JsonResponse

from django.core.serializers import serialize


from rest_framework.decorators import api_view
# Create your views here.



@api_view(["GET",'POST'])
def show_all(request):
    if request.method == "GET":
        query = 'select * from my_app_my_table'

        my_table_var = my_table.objects.raw(query)


        
        my_table_serialzer = serialize('json',my_table_var)
        # my_table_serialzer = MySerializer(my_table_var)
        # my_table_serialzer = serialize(my_table_var)

        # my_table_serialzer = my_table_serialzer.replace('f{\}', '')
        print(my_table_var)
        print("----------------------------")
        print(my_table_serialzer)
        return JsonResponse(my_table_serialzer, safe=False)

    elif request.method == "POST":
        query = "insert into my_app_my_table ('name','age') values (%s,%s)"

        my_table_var = my_table.objects.raw(query, [name,age])

