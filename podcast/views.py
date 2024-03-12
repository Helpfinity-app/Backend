from rest_framework import viewsets, filters, status, pagination, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.functions import get_user_data, login
from podcast.serializers import CatSerializer,PodSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.generics import GenericAPIView
from accounts.models import User
from podcast.models import Category, Podcast
from django.db.models import Q
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework import pagination
from django.shortcuts import render, get_object_or_404


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100






class Categories(APIView):
    serializer_class = CatSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        cats = Category.objects.all()
        serializer = self.serializer_class(cats,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class Podcasts(APIView):
    serializer_class = PodSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        pods = Podcast.objects.all()
        serializer = self.serializer_class(pods,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





class PodcastsFullView(GenericAPIView):
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    serializer_class = PodSerializer
    queryset = Podcast.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id']
    filterset_fields = ['category','id']

    def get(self, request, format=None):
        query = self.filter_queryset(Podcast.objects.all())
        page = self.paginate_queryset(query)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)






class PodcastItem(APIView):
        serializer_class = PodSerializer
        permission_classes = [AllowAny]
        def get(self, request, *args, **kwargs):
            pod = get_object_or_404(Podcast, id=self.kwargs["id"])
            serializer = self.serializer_class(pod)
            return Response(serializer.data)