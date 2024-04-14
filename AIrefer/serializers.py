from rest_framework import serializers
from AIrefer.models import AIrefer_Questions, User_AIrefer_Answer, Thoughts


class AIrefer_QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIrefer_Questions
        fields = "__all__"


class User_AIrefer_AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_AIrefer_Answer
        fields = "__all__"


class ThoughtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thoughts
        fields = "__all__"
