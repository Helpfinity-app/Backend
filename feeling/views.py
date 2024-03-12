from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from feeling.serializers import FeelingSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from feeling.models import Feeling
from django.shortcuts import render, get_object_or_404




class Feelings(APIView):
    serializer_class = FeelingSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        feelings = Feeling.objects.filter(user=self.request.user)
        serializer = self.serializer_class(feelings,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data=self.request.data
        data['user'] = self.request.user.id
        serializer = FeelingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class FeelingItem(APIView):
        serializer_class = FeelingSerializer
        permission_classes = [IsAuthenticated]
        def get(self, request, *args, **kwargs):
            feeling = get_object_or_404(Feeling, id=self.kwargs["id"])
            serializer = self.serializer_class(feeling)
            return Response(serializer.data)