from django.core import serializers
from rest_framework import serializers
from django.contrib.auth.models import User
from medapi.models import Medicine
from rest_framework.serializers import ModelSerializer



class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()
    password_confirmation= serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    

