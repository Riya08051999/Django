from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models
from quiz_api.models import Quizer,Question,Answer,Exam,Feedback,Quiz

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password']
        extra_kwargs={'password':{'write_only':True,'required':True}}
    def create(self, validated_data):
        user=User.objects.create_superuser(**validated_data)
        Token.objects.create(user=user)
        return user

class QuizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizer
        fields = ['username', 'password']
     
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields ="__all__"

                
class ExamSerializer(serializers.ModelSerializer):
    section1=QuizSerializer()
    section2=QuizSerializer()
    section3=QuizSerializer()
    class Meta:
        model=Exam
        fields=['exam','section1','section2','section3']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields=['User_id','name','email','subject','messages']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['quiz', 'questions']
        # extra_kwargs={'password':{'write_only':True,'required':True}}
    def create(self, validated_data):
        ques=Question.objects.create(**validated_data)
        return ques
        

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['questions','answer']
        # extra_kwargs={'password':{'write_only':True,'required':True}}
    def create(self, validated_data):
        ans=Answer.objects.create(**validated_data)
        return ans
