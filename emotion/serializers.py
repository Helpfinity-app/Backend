from rest_framework import serializers
from emotion.models import Emotion


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = "__all__"