from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,HTTP_200_OK)

from django.contrib.auth import authenticate,login
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .serializers import MedicineSerializer
from rest_framework.serializers import ModelSerializer
from medapi.models import Medicine
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token




@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')
    

    if username and password and email and password==password_confirmation:
        user = User.objects.create_user(username=username,email=email, password=password)
        return Response({'message': 'Signup successful'})
    else:
        return Response({'error': 'Invalid data'}, status=400)
    
    

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        token,_ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'message': 'Login successful'}, status=HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=400)

    


@api_view(['POST'])
@permission_classes((AllowAny,))
def logout(request):
    
    return Response({'message': 'Logout successful'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_medicine(request):
    queryset = Medicine.objects.all()
    serializer = MedicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@login_required
def get_all_medicines(request):
    medicines = Medicine.objects.all()
    serializer = MedicineSerializer(medicines, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@login_required
def update_medicine(request, pk):
    try:
        medicine = Medicine.objects.get(pk=pk)
    except Medicine.DoesNotExist:
        return Response({'error': 'Medicine not found'}, status=404)

    serializer = MedicineSerializer(medicine, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@login_required
def delete_medicine(request, pk):
    try:
        medicine = Medicine.objects.get(pk=pk)
    except Medicine.DoesNotExist:
        return Response({'error': 'Medicine not found'}, status=404)

    medicine.delete()
    return Response({'message': 'Medicine deleted'})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_medicine_by_name(request, name):
    medicines = Medicine.objects.filter(name__icontains=name)
    
    if not medicines:
        return Response({'error': 'Medicine not found'}, status=404)
    
    serializer = MedicineSerializer(medicines, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_single_medicine(request, pk):
    try:
        medicine = Medicine.objects.get(pk=pk)
        serializer = MedicineSerializer(medicine)
        return Response(serializer.data)
    except Medicine.DoesNotExist:
        return Response({'error': 'Medicine not found'}, status=404)


   