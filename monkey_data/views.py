from urllib import response
from warnings import catch_warnings
from django.http import JsonResponse
from .models import Monkey
from .serializers import MonkeySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status
from datetime import datetime

from monkey_data import serializers


@api_view(['GET','POST'])

def Monkey_list(request,format=None):

    if request.method == 'GET':
        monkey = Monkey.objects.all()
        serializer = MonkeySerializer(monkey,many =True)
        return JsonResponse(serializer.data,safe=False)
    

    if request.method == 'POST':
        monData = JSONParser().parse(request)
        serializer = MonkeySerializer(data=monData)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print('here ' + str(serializer.errors) + 'end')



'''    
@api_view(['GET'])
def monkey_country_details(request,id):
    try:
        monkey = Monkey.objects.get(pk=id)
    except Monkey.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MonkeySerializer(monkey)
        return Response(serializer.data)
'''   