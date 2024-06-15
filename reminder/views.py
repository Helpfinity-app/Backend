from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from reminder.serializers import ReminderSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from reminder.models import Reminder
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework import pagination
from rest_framework.generics import GenericAPIView
from django_filters.rest_framework import DjangoFilterBackend


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class RemindersFullView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    serializer_class = ReminderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['date_time']
    filterset_fields = ['date_time','id']

    def get(self, request, format=None):
        query = self.filter_queryset(Reminder.objects.filter(user=self.request.user))
        page = self.paginate_queryset(query)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




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

        def delete(self, request, *args, **kwargs):
            reminder = get_object_or_404(Reminder, id=self.kwargs["id"])
            reminder.delete()
            return Response("reminder deleted.")