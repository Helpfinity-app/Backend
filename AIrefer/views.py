from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from AIrefer.serializers import AIrefer_QuestionsSerializer, User_AIrefer_AnswerSerializer, ThoughtsSerializer, AnswerSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from AIrefer.models import AIrefer_Questions, User_AIrefer_Answer, Thoughts, Answer
from django.shortcuts import render, get_object_or_404



class Questions(APIView):
    serializer_class = AIrefer_QuestionsSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        questions = AIrefer_Questions.objects.all()
        serializer = self.serializer_class(questions,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class UserAnswer(APIView):
    serializer_class = User_AIrefer_AnswerSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data=self.request.data
        data['user'] = self.request.user.id
        serializer = User_AIrefer_AnswerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserMultiAnswer(APIView):
    #serializer_class = User_AIrefer_AnswerSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            data = self.request.data
            for Q in data['questions']:
                ai_answers = User_AIrefer_Answer()
                ai_answers.user = self.request.user
                ai_answers.questions = AIrefer_Questions.objects.get(id=Q['question'])
                ai_answers.answer = Q['answer']
                ai_answers.save()
                return Response(data, status=status.HTTP_201_CREATED)
        except:
            return Response("questions not found or other error... try again", status=status.HTTP_400_BAD_REQUEST)



class Thoughts(APIView):
    serializer_class = ThoughtsSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data=self.request.data
        data['user'] = self.request.user.id
        serializer = ThoughtsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ResultView(APIView):
    serializer_class = AIrefer_QuestionsSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        return Response("In preparation...", status=status.HTTP_200_OK)




class AnswersView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        answer = Answer.objects.all()
        serializer = self.serializer_class(answer,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

