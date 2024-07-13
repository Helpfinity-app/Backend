from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from journey.serializers import JourneySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from journey.models import Journey
from django.shortcuts import render, get_object_or_404




class JourneyView(APIView):
    serializer_class = JourneySerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        journey = Journey.objects.filter(user=self.request.user).order_by('-id')[:8]
        serializer = self.serializer_class(journey,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data=self.request.data
        data['user'] = self.request.user.id
        serializer = JourneySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class JourneyItem(APIView):
        serializer_class = JourneySerializer
        permission_classes = [IsAuthenticated]
        def get(self, request, *args, **kwargs):
            journey = get_object_or_404(Journey, id=self.kwargs["id"])
            serializer = self.serializer_class(journey)
            return Response(serializer.data)