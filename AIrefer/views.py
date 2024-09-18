from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from AIrefer.serializers import AIrefer_QuestionsSerializer, User_AIrefer_AnswerSerializer, ThoughtsSerializer, AnswerSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.models import User
from AIrefer.models import AIrefer_Questions, User_AIrefer_Answer, Thoughts, Answer
from django.shortcuts import render, get_object_or_404
from journey.serializers import JourneySerializer, BreathSerializer
from datetime import datetime
from openai import OpenAI
from django.utils import timezone





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
        data['level'] = 3
        data['date'] = datetime.now().strftime('%A')
        serializer = ThoughtsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            jserializer = JourneySerializer(data=data, partial=True)
            if jserializer.is_valid():
                jserializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



client = OpenAI(api_key='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')

class ResultView(APIView):
    serializer_class = AIrefer_QuestionsSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        today = timezone.now().date()
        question_answers = User_AIrefer_Answer.objects.filter(user=self.request.user,date_time__date=today)
        user_answers = ""
        for item in question_answers:
            user_answers += "\n \n"
            user_answers += item.questions.questions
            user_answers += "\n"
            user_answers += item.answer

        prompt = "This is a list of psychological questions with their answers related to a person." \
                 "{} \n Based on this person's answers, do a psychological analysis of his situation and give him a report and help him get better and don't ask him any more questions.".format(user_answers)

        response = client.completions.create(model="gpt-3.5-turbo-instruct",prompt=prompt,max_tokens=150)
        answer = response.choices[0].text.strip()
        return Response(answer, status=status.HTTP_200_OK)



class AnswersView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        answer = Answer.objects.all()
        serializer = self.serializer_class(answer,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
