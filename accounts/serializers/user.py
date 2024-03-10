from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id","username","email","first_name","last_name","created_at","updated_at","is_active","is_superuser","email_verified")


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email","password")


class UserAllFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"



class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email","password")