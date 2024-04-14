from rest_framework import serializers
from behavior.models import UserBehavior, Behavior


class BehaviorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behavior
        fields = "__all__"


class UserBehaviorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBehavior
        fields = "__all__"


class UserShortBehaviorSerializer(serializers.ModelSerializer):
    behavior = BehaviorSerializer()
    class Meta:
        model = UserBehavior
        fields = ("behavior", "date_time")
