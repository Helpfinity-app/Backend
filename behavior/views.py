from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from behavior.serializers import UserBehaviorSerializer, BehaviorSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from behavior.models import Behavior,UserBehavior
from django.shortcuts import render, get_object_or_404




class Behaviors(APIView):
    serializer_class = BehaviorSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        behaviors = Behavior.objects.filter(user=self.request.user)
        serializer = self.serializer_class(behaviors,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data=self.request.data
        data['user'] = self.request.user.id
        serializer = BehaviorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserBehavior(APIView):
    serializer_class = UserBehaviorSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data=self.request.data
        data['user'] = self.request.user.id
        serializer = UserBehaviorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
