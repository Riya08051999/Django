
from django.contrib import admin
from django.urls import path

from django.urls import include, path
from rest_framework import routers

from quiz_api import views



router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

router.register('question', views.QuestionViewSet)
router.register('exam', views.ExamViewSet)
router.register('feedback', views.FeedbackViewSet)
router.register('Quiz', views.QuizViewSet)
 

 
urlpatterns = [
         path('', include(router.urls)),
        path('quizer/',views.quizerUser,name="quizer"),
        
]