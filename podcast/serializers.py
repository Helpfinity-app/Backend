from rest_framework import serializers
from podcast.models import Category,Podcast



class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = "__all__"


class PodFullSerializer(serializers.ModelSerializer):
    category = CatSerializer()
    class Meta:
        model = Podcast
        fields = "__all__"
