from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from reminder.serializers import ReminderSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from reminder.models import Reminder
from django.shortcuts import render, get_object_or_404




class Reminders(APIView):
    serializer_class = ReminderSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        reminders = Reminder.objects.filter(user=self.request.user)
        serializer = self.serializer_class(reminders,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data=self.request.data
        data['user'] = self.request.user.id
        serializer = ReminderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ReminderItem(APIView):
        serializer_class = ReminderSerializer
        permission_classes = [IsAuthenticated]
        def get(self, request, *args, **kwargs):
            reminder = get_object_or_404(Reminder, id=self.kwargs["id"])
            serializer = self.serializer_class(reminder)
            return Response(serializer.data)