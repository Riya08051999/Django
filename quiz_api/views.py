from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quiz_api.serializers import UserSerializer,QuizerSerializer,\
    QuestionSerializer,AnswerSerializer,FeedbackSerializer,ExamSerializer,QuizSerializer
from quiz_api.models import Quizer,Question,Answer,Feedback,Exam,Quiz
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response




class UserViewSet(viewsets.ModelViewSet):
   
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset=Quiz.objects.all()
    serializer_class=QuizSerializer    
    
class ExamViewSet(viewsets.ModelViewSet):
    queryset=Exam.objects.all()
    serializer_class=ExamSerializer   

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset=Feedback.objects.all()
    serializer_class=FeedbackSerializer




@api_view(['GET', 'POST'])
def quizerUser(request):
    if request.method == 'POST':
        data=request.data
        if Quizer.objects.filter(username=data['username'],password=data['password']).exists():
            user=Quizer.objects.filter(username=data['username'])
            serializer = QuizerSerializer(user, many=True)
            return Response(serializer.data)
        
        else:
            serializer = QuizerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    