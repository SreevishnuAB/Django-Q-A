from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from rest_framework.views import APIView

from quora.models import Answer, Like, Question

# Create your views here.
def login(request):
    return render(request, 'quora/login.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home(request):
    questions = Question.objects.all().order_by("-created_at")
    # print(question[])
    return render(request, "home.html", {"questions": questions})


class QuestionsView(APIView):

    def get(self, request):
        questions = Question.objects.all().order_by("-created_at")
        return render(request, "home.html", {"questions": questions})
    
    def post(self, request):
        question_text = request.POST.get("question_text")
        question = Question(question_text=question_text)
        user = request.user
        question.created_by = user
        question.save()
        return redirect("/")
    
    def delete(self, request, question_id):
        question = Question.objects.get(id=question_id)
        question.delete()
        return redirect("/")


class AnswersView(APIView):

    def post(self, request, question_id):
        answer_text = request.POST.get("answer_text")
        question = Question.objects.get(id=question_id)
        user = request.user
        answer = Answer(question=question, answer_text=answer_text, created_by=user)
        answer.save()
        return redirect("/")
    
    def delete(self, request, question_id, answer_id):
        answer = Answer.objects.get(id=answer_id)
        answer.delete()
        questions = Question.objects.all().order_by("-created_at")
        return redirect("/")
    

class LikesView(APIView):

    def post(self, request, question_id, answer_id):
        answer = Answer.objects.get(id=answer_id)
        user = request.user
        # Check if the user has already liked the answer
        if not Like.objects.filter(answer=answer, user=user).exists():
            like = Like(answer=answer, user=user)
            like.save()
        return redirect("/")
    
    def delete(self, request, question_id, answer_id):
        like = Like.objects.get(answer_id=answer_id, user=request.user)
        like.delete()
        return redirect("/")