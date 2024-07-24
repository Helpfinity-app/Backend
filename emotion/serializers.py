from rest_framework import serializers
from emotion.models import Emotion, Depression, Anxitey

class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = "__all__"

class AnxiteySerializer(serializers.ModelSerializer):
    class Meta:
        model = Anxitey
        fields = "__all__"

class DepressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depression
        fields = "__all__"