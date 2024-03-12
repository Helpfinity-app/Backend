from rest_framework import serializers
from feeling.models import Feeling


class FeelingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeling
        fields = "__all__"
