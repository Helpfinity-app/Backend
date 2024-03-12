from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.functions import get_user_data, login
from podcast.serializers import CatSerializer,PodSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from podcast.models import Category, Podcast


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
