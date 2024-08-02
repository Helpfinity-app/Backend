from rest_framework import serializers
from journey.models import Journey, Breath


class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = "__all__"


class BreathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breath
        fields = "__all__"