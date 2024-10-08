from rest_framework import serializers
from emotion.models import Emotion, Depression, Anxitey, Answer

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = "__all__"

class EmotionChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = ("feeling","date_time")

class AnxiteySerializer(serializers.ModelSerializer):
    class Meta:
        model = Anxitey
        fields = "__all__"

class DepressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depression
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
