from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from feeling.serializers import FeelingShortSerializer
from behavior.serializers import UserShortBehaviorSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from behavior.models import UserBehavior
from feeling.models import Feeling


class Analyze(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):

        feeling = Feeling.objects.filter(user=self.request.user)
        feeling_serializer = FeelingShortSerializer(feeling,many=True)

        behavior = UserBehavior.objects.filter(user=self.request.user)
        behavior_serializer = UserShortBehaviorSerializer(behavior, many=True)

        data = {"mood_chart":feeling_serializer.data,"emotions":behavior_serializer.data}
        return Response(data, status=status.HTTP_200_OK)