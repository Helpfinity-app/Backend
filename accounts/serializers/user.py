from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id","username","email","first_name","last_name","created_at","updated_at","is_active","is_superuser")





class UserAllFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"



class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("first_name","last_name","first_Language","birth_date","national_code","city")


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "first_name")
        extra_kwargs = {
            "email": {"required": False},
            "first_name": {"required": True},
        }

