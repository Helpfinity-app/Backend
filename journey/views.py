from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from journey.serializers import JourneySerializer, BreathSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from journey.models import Journey, Breath
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from journey.serializers import JourneySerializer, BreathSerializer
from datetime import datetime


class JourneyStepsView(APIView):
    serializer_class = JourneySerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        today = timezone.now()
        journey = Journey.objects.filter(date_time__date=today.date()).order_by('-level').first()
        if journey:
            serializer = self.serializer_class(journey)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("No journeys found for today.", status=status.HTTP_404_NOT_FOUND)




class JourneyView(APIView):
    serializer_class = JourneySerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        eight_days_ago = timezone.now() - timedelta(days=8)
        journeys = Journey.objects.filter(user=self.request.user, date_time__gte=eight_days_ago)
        # Get the journey with the highest level for each day
        result = []
        for day in range(8):
            day_start = eight_days_ago + timedelta(days=day)
            day_end = day_start + timedelta(days=1)
            max_level_journey = journeys.filter(date_time__gte=day_start, date_time__lt=day_end).order_by('-level').first()
            if max_level_journey:
                result.append(max_level_journey)
        serializer = self.serializer_class(result, many=True)
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



class BreathView(APIView):
    serializer_class = BreathSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        one_days_ago = timezone.now() - timedelta(days=1)
        breath = Breath.objects.filter(user=self.request.user,date_time__gte=one_days_ago)
        if breath:
            is_breath = True
        else:
            is_breath = False
        return Response(is_breath, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data=self.request.data
        data['user'] = self.request.user.id
        data['level'] = 2
        data['date'] = datetime.now().strftime('%A')
        serializer = BreathSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            jserializer = JourneySerializer(data=data, partial=True)
            if jserializer.is_valid():
                jserializer.save()
            return Response("Breath added.", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
