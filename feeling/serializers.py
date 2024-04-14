from rest_framework import serializers
from feeling.models import Feeling


class FeelingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeling
        fields = "__all__"



class FeelingShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeling
        fields = ("feeling", "date_time")
