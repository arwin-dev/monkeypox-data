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


@api_view(['GET','POST'])

def Monkey_list(request):

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
        