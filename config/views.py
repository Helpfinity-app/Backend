from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from podcast.serializers import PodFullSerializer
from rest_framework.permissions import AllowAny
from podcast.models import Category, Podcast
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


class Landing(APIView):
    serializer_class = PodFullSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        pods = Podcast.objects.all()
        last_5_items = pods.reverse()[:5]
        serializer = self.serializer_class(last_5_items,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
