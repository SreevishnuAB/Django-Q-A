"""
URL configuration for q_and_a project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from quora.views import LikesView, SignUpView, QuestionsView, AnswersView, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup", SignUpView.as_view(), name="signup"),
    path("", home, name="home"),
    path("questions/", QuestionsView.as_view(), name="questions"),
    path("questions/<int:question_id>/", QuestionsView.as_view(), name="question_delete"),
    path("questions/<int:question_id>/answers", AnswersView.as_view(), name="answers"),
    path("questions/<int:question_id>/answers/<int:answer_id>/", AnswersView.as_view(), name="delete_answer"),
    path("questions/<int:question_id>/answers/<int:answer_id>/like", LikesView.as_view(), name="unlike/like_answer"),
]
