from django.shortcuts import render
from rest_framework.response import Response
from .models import User, Notify
from .serializers import UserSerializer, NotifySerializer
from rest_framework.decorators import api_view

from api import serializers
#link
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'Get All': '/get-all',
        'Create User': '/create-user',
        'Create Notify' : '/create-notify',
        'Delete User': '/delete-user/idUser/',
        'Delete Notify': '/delete-notify/idNotify/',
    }
    return Response(api_urls)

#Lay tat ca
@api_view(['GET'])
def getAll(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

#Them user
@api_view(['POST'])
def createUser(request):
    serializers = UserSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

#Them notify
@api_view(['POST'])
def createNotify(request):
    serializers = NotifySerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

#Xoa user
@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(idUser=pk)
    user.delete()
    return Response("Succesfully delete!")

#Xoa thong bao
@api_view(['DELETE'])
def deleteNotify(request, pk):
    notify = Notify.objects.get(idNotify=pk)
    notify.delete()
    return Response("Succesfully delete!")
