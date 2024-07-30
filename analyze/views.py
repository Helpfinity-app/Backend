from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from emotion.serializers import EmotionChartSerializer, EmotionSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from emotion.models import Emotion
import ast
from collections import Counter
from behavior.models import UserBehavior



class Mood(APIView):
    serializer_class = EmotionChartSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        emotions = Emotion.objects.filter(user=self.request.user).order_by('-date_time')[:7]
        serializer = self.serializer_class(emotions,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class TopPositive(APIView):
    serializer_class = EmotionSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        emotions = Emotion.objects.filter(user=self.request.user).order_by('-date_time')[:7]
        combined_list = []
        for obj in emotions:
            list_of_items = ast.literal_eval(obj.positive)
            for item in list_of_items:
                combined_list.append(item)
        counter = Counter(combined_list)
        sorted_data = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        num = 1
        top_positive = []
        for obj in sorted_data:
            if num <= 5:
                top_positive.append({"number": num, "label": obj[0]})
                num += 1
        return Response(top_positive, status=status.HTTP_200_OK)



class TopNegative(APIView):
    serializer_class = EmotionSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        emotions = Emotion.objects.filter(user=self.request.user).order_by('-date_time')[:7]
        combined_list = []
        for obj in emotions:
            list_of_items = ast.literal_eval(obj.negative)
            for item in list_of_items:
                combined_list.append(item)
        counter = Counter(combined_list)
        sorted_data = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        num = 1
        top_negative = []
        for obj in sorted_data:
            if num <= 5:
                top_negative.append({"number": num, "label": obj[0]})
                num += 1
        return Response(top_negative, status=status.HTTP_200_OK)


class TopBehavior(APIView):
    serializer_class = EmotionSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        behavior = UserBehavior.objects.filter(user=self.request.user).order_by('-date_time')[:7]
        combined_list = []
        for obj in behavior:
            combined_list.append(obj.behavior.behavior)
        counter = Counter(combined_list)
        sorted_data = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        num = 1
        top_behavior = []
        for obj in sorted_data:
            if num <= 4:
                top_behavior.append({"number": num, "label": obj[0]})
                num += 1
        return Response(top_behavior, status=status.HTTP_200_OK)


class Full(APIView):
    serializer_class = EmotionChartSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        emotions = Emotion.objects.filter(user=self.request.user).order_by('-date_time')[:7]
        serializer = self.serializer_class(emotions,many=True)

        combined_list = []
        for obj in emotions:
            list_of_items = ast.literal_eval(obj.positive)
            for item in list_of_items:
                combined_list.append(item)
        counter = Counter(combined_list)
        sorted_data = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        num = 1
        top_positive = []
        for obj in sorted_data:
            if num <= 5:
                top_positive.append({"number": num, "label": obj[0]})
                num += 1

        combined_list2 = []
        for obj in emotions:
            list_of_items = ast.literal_eval(obj.negative)
            for item in list_of_items:
                combined_list2.append(item)
        counter2 = Counter(combined_list2)
        sorted_data2 = sorted(counter2.items(), key=lambda x: (-x[1], x[0]))
        num = 1
        top_negative = []
        for obj in sorted_data2:
            if num <= 5:
                top_negative.append({"number": num, "label": obj[0]})
                num += 1


        behavior = UserBehavior.objects.filter(user=self.request.user).order_by('-date_time')[:7]
        combined_list3 = []
        for obj in behavior:
            combined_list3.append(obj.behavior.behavior)
        counter3 = Counter(combined_list3)
        sorted_data3 = sorted(counter3.items(), key=lambda x: (-x[1], x[0]))
        num = 1
        top_behavior = []
        for obj in sorted_data3:
            if num <= 4:
                top_behavior.append({"number": num, "label": obj[0]})
                num += 1

        full_data = {"mood":serializer.data, "top_positive":top_positive, "top_negative":top_negative, "top_behavior":top_behavior}
        return Response(full_data, status=status.HTTP_200_OK)
