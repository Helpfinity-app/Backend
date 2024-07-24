from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from emotion.serializers import EmotionSerializer, DepressionSerializer, AnxiteySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from emotion.models import Emotion, Depression, Anxitey
from django.shortcuts import render, get_object_or_404



class Emotions(APIView):
    serializer_class = EmotionSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        emotion = Emotion.objects.filter(user=self.request.user)
        serializer = self.serializer_class(emotion,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data=self.request.data
        data['user'] = self.request.user.id
        serializer = EmotionSerializer(data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmotionItem(APIView):
        serializer_class = EmotionSerializer
        permission_classes = [IsAuthenticated]
        def get(self, request, *args, **kwargs):
            emotion = get_object_or_404(Emotion, id=self.kwargs["id"])
            serializer = self.serializer_class(emotion)
            return Response(serializer.data)







class Depressions(APIView):
    serializer_class = DepressionSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        depression = Depression.objects.filter(user=self.request.user)
        serializer = self.serializer_class(depression,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data=self.request.data
        data['user'] = self.request.user.id
        serializer = DepressionSerializer(data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepressionItem(APIView):
        serializer_class = DepressionSerializer
        permission_classes = [IsAuthenticated]
        def get(self, request, *args, **kwargs):
            depression = get_object_or_404(Depression, id=self.kwargs["id"])
            serializer = self.serializer_class(depression)
            return Response(serializer.data)








class Anxieties(APIView):
    serializer_class = AnxiteySerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        anxitey = Anxitey.objects.filter(user=self.request.user)
        serializer = self.serializer_class(anxitey,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data=self.request.data
        data['user'] = self.request.user.id
        serializer = AnxiteySerializer(data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnxiteyItem(APIView):
        serializer_class = AnxiteySerializer
        permission_classes = [IsAuthenticated]
        def get(self, request, *args, **kwargs):
            anxitey = get_object_or_404(Anxitey, id=self.kwargs["id"])
            serializer = self.serializer_class(anxitey)
            return Response(serializer.data)