from django.db import models
from django.contrib.auth.models import User


class Quizer(models.Model):
    username=models.CharField(max_length=50,blank=False,primary_key=True)
    password=models.CharField(max_length=50,blank=False)
	
	
class Quiz(models.Model):
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=None)
	title = models.CharField(max_length=255, default='')
	created_at = models.DateTimeField(auto_now_add=True)
	times_taken = models.IntegerField(default=0, editable=False)

	@property
	def question_count(self):
		return self.questions.count()
	
	class Meta:
		verbose_name_plural = "Quizzes"
		ordering = ['id']

	def __str__(self):
		return self.title

class Question(models.Model):
	quiz = models.ForeignKey(
		Quiz, 
		related_name='questions', 
		on_delete=models.DO_NOTHING
	)
	questions= models.CharField(max_length=255, default='')

	class Meta:
    		ordering = ['id']

	def __str__(self):
		return self.questions

class Answer(models.Model):
	question = models.ForeignKey(
		Question, 
		related_name='answers', 
		on_delete=models.DO_NOTHING
	)
	text = models.CharField(max_length=255)
	correct = models.BooleanField(default=False)

	def __str__(self):
		return self.text

class Exam(models.Model):
	exam=models.AutoField(primary_key=True)
	section1=models.ForeignKey(Quiz,related_name="section1",on_delete=models.CASCADE)
	section2=models.ForeignKey(Quiz,related_name="section2",on_delete=models.CASCADE)
	section3=models.ForeignKey(Quiz,related_name="section3",on_delete=models.CASCADE)

class Feedback(models.Model):
	User_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100,default="")
	email=models.CharField(max_length=100,default="")
	subject=models.CharField(max_length=100,default="")
	messages=models.CharField(max_length=200,default="")