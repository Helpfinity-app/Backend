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
from django.db.models.functions import TruncDate,TruncDay
from datetime import timedelta
from django.db.models import F
from django.db.models import Avg
from django.utils import timezone
import random



class Mood(APIView):
    serializer_class = EmotionChartSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        seven_days_ago = timezone.now() - timedelta(days=7)
        last_7_days_emotions = Emotion.objects.filter(user=self.request.user,date_time__gte=seven_days_ago)
        average_feelings = last_7_days_emotions.annotate(day=TruncDay('date_time')).values('day').annotate(average_feeling_rate=Avg('feeling_rate')).order_by('day')
        response = []
        for entry in average_feelings:
            obj = {"Date":entry['day'], "Average Feeling":entry['average_feeling_rate']}
            response.append(obj)
        return Response(response, status=status.HTTP_200_OK)



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
        if len(sorted_data) >= 5:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_positive.append({"x": 40, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_positive.append({"x": 10, "y": 35, "z": 30, "label": obj[0]})
                    elif num == 3:
                        top_positive.append({"x": 90, "y": 40, "z": 30, "label": obj[0]})
                    elif num == 4:
                        top_positive.append({"x": 63, "y": 39, "z": 25, "label": obj[0]})
                    elif num == 5:
                        top_positive.append({"x": 66, "y": 65, "z": 20, "label": obj[0]})
                    num += 1
        elif len(sorted_data) == 4:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_positive.append({"x": 40, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_positive.append({"x": 10, "y": 35, "z": 30, "label": obj[0]})
                    elif num == 3:
                        top_positive.append({"x": 90, "y": 40, "z": 30, "label": obj[0]})
                    elif num == 4:
                        top_positive.append({"x": 63, "y": 39, "z": 25, "label": obj[0]})
                        top_positive.append({"x": 66, "y": 65, "z": 0, "label":""})
                    num += 1
        elif len(sorted_data) == 3:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_positive.append({"x": 40, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_positive.append({"x": 10, "y": 35, "z": 30, "label": obj[0]})
                    elif num == 3:
                        top_positive.append({"x": 90, "y": 40, "z": 30, "label": obj[0]})
                        top_positive.append({"x": 63, "y": 39, "z": 0, "label": ""})
                        top_positive.append({"x": 66, "y": 65, "z": 0, "label": ""})
                    num += 1
        elif len(sorted_data) == 2:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_positive.append({"x": 40, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_positive.append({"x": 10, "y": 35, "z": 30, "label": obj[0]})
                        top_positive.append({"x": 90, "y": 40, "z": 0, "label": ""})
                        top_positive.append({"x": 63, "y": 39, "z": 0, "label": ""})
                        top_positive.append({"x": 66, "y": 65, "z": 0, "label": ""})
                    num += 1
        elif len(sorted_data) == 1:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_positive.append({"x": 40, "y": 45, "z": 35, "label": obj[0]})
                        top_positive.append({"x": 10, "y": 35, "z": 0, "label": ""})
                        top_positive.append({"x": 90, "y": 40, "z": 0, "label": ""})
                        top_positive.append({"x": 63, "y": 39, "z": 0, "label": ""})
                        top_positive.append({"x": 66, "y": 65, "z": 0, "label": ""})
                    num += 1
        else:
            top_positive.append({"x": 40, "y": 45, "z": 0, "label": ""})
            top_positive.append({"x": 10, "y": 35, "z": 0, "label": ""})
            top_positive.append({"x": 90, "y": 40, "z": 0, "label": ""})
            top_positive.append({"x": 63, "y": 39, "z": 0, "label": ""})
            top_positive.append({"x": 66, "y": 65, "z": 0, "label": ""})

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
        if len(sorted_data) >= 5:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_negative.append({"x": 15, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_negative.append({"x": 90, "y": 65, "z": 30, "label": obj[0]})
                    elif num == 3:
                        top_negative.append({"x": 52, "y": 50, "z": 25, "label": obj[0]})
                    elif num == 4:
                        top_negative.append({"x": 72, "y": 30, "z": 25, "label": obj[0]})
                    elif num == 5:
                        top_negative.append({"x": 34, "y": 25, "z": 20, "label": obj[0]})
                    num += 1
        elif len(sorted_data) == 4:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_negative.append({"x": 15, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_negative.append({"x": 90, "y": 65, "z": 30, "label": obj[0]})
                    elif num == 3:
                        top_negative.append({"x": 52, "y": 50, "z": 25, "label": obj[0]})
                    elif num == 4:
                        top_negative.append({"x": 72, "y": 30, "z": 25, "label": obj[0]})
                        top_negative.append({"x": 34, "y": 25, "z": 0, "label": ""})
                    num += 1
        elif len(sorted_data) == 3:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_negative.append({"x": 15, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_negative.append({"x": 90, "y": 65, "z": 30, "label": obj[0]})
                    elif num == 3:
                        top_negative.append({"x": 52, "y": 50, "z": 25, "label": obj[0]})
                        top_negative.append({"x": 72, "y": 30, "z": 0, "label": ""})
                        top_negative.append({"x": 34, "y": 25, "z": 0, "label": ""})
                    num += 1
        elif len(sorted_data) == 2:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_negative.append({"x": 15, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_negative.append({"x": 90, "y": 65, "z": 30, "label": obj[0]})
                        top_negative.append({"x": 52, "y": 50, "z": 0, "label": ""})
                        top_negative.append({"x": 72, "y": 30, "z": 0, "label": ""})
                        top_negative.append({"x": 34, "y": 25, "z": 0, "label": ""})
                    num += 1
        elif len(sorted_data) == 1:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_negative.append({"x": 15, "y": 45, "z": 35, "label": obj[0]})
                        top_negative.append({"x": 90, "y": 65, "z": 0, "label": ""})
                        top_negative.append({"x": 52, "y": 50, "z": 0, "label": ""})
                        top_negative.append({"x": 72, "y": 30, "z": 0, "label": ""})
                        top_negative.append({"x": 34, "y": 25, "z": 0, "label": ""})
                    num += 1
        else:
            top_negative.append({"x": 15, "y": 45, "z": 0, "label": ""})
            top_negative.append({"x": 90, "y": 65, "z": 0, "label": ""})
            top_negative.append({"x": 52, "y": 50, "z": 0, "label": ""})
            top_negative.append({"x": 72, "y": 30, "z": 0, "label": ""})
            top_negative.append({"x": 34, "y": 25, "z": 0, "label": ""})

        return Response(top_negative, status=status.HTTP_200_OK)


class TopBehavior(APIView):
    serializer_class = EmotionSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        behavior = UserBehavior.objects.filter(user=self.request.user).order_by('-date_time')[:7]
        if behavior:
            combined_list = []
            for obj in behavior:
                combined_list.append(obj.behavior.behavior)
            counter = Counter(combined_list)
            sorted_data = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

            top_behavior = []
            lst = []
            for obj in sorted_data:
                lst.append(obj[1])
            total = sum(lst)
            scale_factor = 360 / total
            for x in sorted_data:
                item = {"label": x[0], "value": x[1] * scale_factor,
                        "color": "#{:06x}".format(random.randint(0, 0xFFFFFF))}
                top_behavior.append(item)
        else:
            top_behavior = []

        return Response(top_behavior, status=status.HTTP_200_OK)




class Full(APIView):
    serializer_class = EmotionChartSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        seven_days_ago = timezone.now() - timedelta(days=7)
        last_7_days_emotions = Emotion.objects.filter(user=self.request.user, date_time__gte=seven_days_ago)
        average_feelings = last_7_days_emotions.annotate(day=TruncDay('date_time')).values('day').annotate(
            average_feeling_rate=Avg('feeling_rate')).order_by('day')
        mood = []
        for entry in average_feelings:
            obj = {"Date": entry['day'], "Average Feeling": entry['average_feeling_rate']}
            mood.append(obj)


        combined_list = []
        for obj in last_7_days_emotions:
            list_of_items = ast.literal_eval(obj.positive)
            for item in list_of_items:
                combined_list.append(item)
        counter = Counter(combined_list)
        sorted_data = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

        num = 1
        top_positive = []
        if len(sorted_data) >= 5:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_positive.append({"x": 40, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_positive.append({"x": 10, "y": 35, "z": 30, "label": obj[0]})
                    elif num == 3:
                        top_positive.append({"x": 90, "y": 40, "z": 30, "label": obj[0]})
                    elif num == 4:
                        top_positive.append({"x": 63, "y": 39, "z": 25, "label": obj[0]})
                    elif num == 5:
                        top_positive.append({"x": 66, "y": 65, "z": 20, "label": obj[0]})
                    num += 1
        elif len(sorted_data) == 4:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_positive.append({"x": 40, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_positive.append({"x": 10, "y": 35, "z": 30, "label": obj[0]})
                    elif num == 3:
                        top_positive.append({"x": 90, "y": 40, "z": 30, "label": obj[0]})
                    elif num == 4:
                        top_positive.append({"x": 63, "y": 39, "z": 25, "label": obj[0]})
                        top_positive.append({"x": 66, "y": 65, "z": 0, "label": ""})
                    num += 1
        elif len(sorted_data) == 3:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_positive.append({"x": 40, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_positive.append({"x": 10, "y": 35, "z": 30, "label": obj[0]})
                    elif num == 3:
                        top_positive.append({"x": 90, "y": 40, "z": 30, "label": obj[0]})
                        top_positive.append({"x": 63, "y": 39, "z": 0, "label": ""})
                        top_positive.append({"x": 66, "y": 65, "z": 0, "label": ""})
                    num += 1
        elif len(sorted_data) == 2:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_positive.append({"x": 40, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_positive.append({"x": 10, "y": 35, "z": 30, "label": obj[0]})
                        top_positive.append({"x": 90, "y": 40, "z": 0, "label": ""})
                        top_positive.append({"x": 63, "y": 39, "z": 0, "label": ""})
                        top_positive.append({"x": 66, "y": 65, "z": 0, "label": ""})
                    num += 1
        elif len(sorted_data) == 1:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_positive.append({"x": 40, "y": 45, "z": 35, "label": obj[0]})
                        top_positive.append({"x": 10, "y": 35, "z": 0, "label": ""})
                        top_positive.append({"x": 90, "y": 40, "z": 0, "label": ""})
                        top_positive.append({"x": 63, "y": 39, "z": 0, "label": ""})
                        top_positive.append({"x": 66, "y": 65, "z": 0, "label": ""})
                    num += 1
        else:
            top_positive.append({"x": 40, "y": 45, "z": 0, "label": ""})
            top_positive.append({"x": 10, "y": 35, "z": 0, "label": ""})
            top_positive.append({"x": 90, "y": 40, "z": 0, "label": ""})
            top_positive.append({"x": 63, "y": 39, "z": 0, "label": ""})
            top_positive.append({"x": 66, "y": 65, "z": 0, "label": ""})




        combined_list2 = []
        for obj in last_7_days_emotions:
            list_of_items = ast.literal_eval(obj.negative)
            for item in list_of_items:
                combined_list2.append(item)
        counter2 = Counter(combined_list2)
        sorted_data2 = sorted(counter2.items(), key=lambda x: (-x[1], x[0]))

        num = 1
        top_negative = []
        if len(sorted_data) >= 5:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_negative.append({"x": 15, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_negative.append({"x": 90, "y": 65, "z": 30, "label": obj[0]})
                    elif num == 3:
                        top_negative.append({"x": 52, "y": 50, "z": 25, "label": obj[0]})
                    elif num == 4:
                        top_negative.append({"x": 72, "y": 30, "z": 25, "label": obj[0]})
                    elif num == 5:
                        top_negative.append({"x": 34, "y": 25, "z": 20, "label": obj[0]})
                    num += 1
        elif len(sorted_data) == 4:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_negative.append({"x": 15, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_negative.append({"x": 90, "y": 65, "z": 30, "label": obj[0]})
                    elif num == 3:
                        top_negative.append({"x": 52, "y": 50, "z": 25, "label": obj[0]})
                    elif num == 4:
                        top_negative.append({"x": 72, "y": 30, "z": 25, "label": obj[0]})
                        top_negative.append({"x": 34, "y": 25, "z": 0, "label": ""})
                    num += 1
        elif len(sorted_data) == 3:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_negative.append({"x": 15, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_negative.append({"x": 90, "y": 65, "z": 30, "label": obj[0]})
                    elif num == 3:
                        top_negative.append({"x": 52, "y": 50, "z": 25, "label": obj[0]})
                        top_negative.append({"x": 72, "y": 30, "z": 0, "label": ""})
                        top_negative.append({"x": 34, "y": 25, "z": 0, "label": ""})
                    num += 1
        elif len(sorted_data) == 2:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_negative.append({"x": 15, "y": 45, "z": 35, "label": obj[0]})
                    elif num == 2:
                        top_negative.append({"x": 90, "y": 65, "z": 30, "label": obj[0]})
                        top_negative.append({"x": 52, "y": 50, "z": 0, "label": ""})
                        top_negative.append({"x": 72, "y": 30, "z": 0, "label": ""})
                        top_negative.append({"x": 34, "y": 25, "z": 0, "label": ""})
                    num += 1
        elif len(sorted_data) == 1:
            for obj in sorted_data:
                if num <= 5:
                    if num == 1:
                        top_negative.append({"x": 15, "y": 45, "z": 35, "label": obj[0]})
                        top_negative.append({"x": 90, "y": 65, "z": 0, "label": ""})
                        top_negative.append({"x": 52, "y": 50, "z": 0, "label": ""})
                        top_negative.append({"x": 72, "y": 30, "z": 0, "label": ""})
                        top_negative.append({"x": 34, "y": 25, "z": 0, "label": ""})
                    num += 1
        else:
            top_negative.append({"x": 15, "y": 45, "z": 0, "label": ""})
            top_negative.append({"x": 90, "y": 65, "z": 0, "label": ""})
            top_negative.append({"x": 52, "y": 50, "z": 0, "label": ""})
            top_negative.append({"x": 72, "y": 30, "z": 0, "label": ""})
            top_negative.append({"x": 34, "y": 25, "z": 0, "label": ""})


        behavior = UserBehavior.objects.filter(user=self.request.user).order_by('-date_time')[:7]
        if behavior:
            combined_list3 = []
            for obj in behavior:
                combined_list3.append(obj.behavior.behavior)
            counter3 = Counter(combined_list3)
            sorted_data3 = sorted(counter3.items(), key=lambda x: (-x[1], x[0]))

            top_behavior = []
            lst = []
            for obj in sorted_data3:
                lst.append(obj[1])
            total = sum(lst)
            scale_factor = 360 / total
            for x in sorted_data3:
                item = {"label": x[0], "value": x[1] * scale_factor,
                        "color": "#{:06x}".format(random.randint(0, 0xFFFFFF))}
                top_behavior.append(item)
        else:
            top_behavior = []

        full_data = {"mood":mood, "top_positive":top_positive, "top_negative":top_negative, "top_behavior":top_behavior}
        return Response(full_data, status=status.HTTP_200_OK)