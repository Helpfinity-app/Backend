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
from openai import OpenAI
from django.http import JsonResponse


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



class ThoughtsView(APIView):
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
            # sth to do about result...
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ResultView(APIView):
    serializer_class = AIrefer_QuestionsSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        '''
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
        '''
        return Response("---", status=status.HTTP_200_OK)



class AnswersView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [AllowAny]
    def get(self, *args, **kwargs):
        answer = Answer.objects.all()
        serializer = self.serializer_class(answer,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ThoughtsResult(APIView):
    serializer_class = ThoughtsSerializer
    permission_classes = [IsAuthenticated]
    def get(self, *args, **kwargs):
        thought = Thoughts.objects.filter(user=self.request.user).last()
        assistant = "You are a bot whose sole function is to identify negative thought patterns such as overgeneralization, black-and-white thinking, catastrophizing, personalization, filtering, mind reading, 'should' and 'must' statements, jumping to conclusions, magnification or minimization, labeling, and emotional reasoning that the user provides to you.\n Your tasks are: 1- Reflect the Negative Pattern and Provide an Explanation: Identify the specific negative thinking pattern present in the user's thought and inform them about it, including a brief explanation of this pattern.  2- Rewrite the User's Thought in an Appropriate Way: Reconstruct the user's thought optimally, transforming it into a more balanced and positive perspective. \n You are to perform only and exclusively these two functions."
        if thought:
            try:
                client = OpenAI(
                    api_key="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")
                response = client.chat.completions.create(
                    model="gpt-4",  # Replace with your desired model gpt-4o-mini
                    messages=[
                        {"role": "user", "content": "{}".format(thought.thoughts)},
                        {"role": "system", "content": assistant},
                    ],
                    max_tokens=150,  # Adjust as needed
                    stop=None,
                    temperature=0.7)
                #final_response = response.choices[0].message['content']
                response_dict = response.model_dump()
                message_content = response_dict['choices'][0]['message']['content']

            except Exception as e:
                return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(message_content, status=status.HTTP_200_OK)
        else:
            return Response("No thought found for this user", status=status.HTTP_400_BAD_REQUEST)
