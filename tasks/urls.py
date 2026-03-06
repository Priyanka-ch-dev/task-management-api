from django.urls import path
from .views import *

urlpatterns = [

path('register',RegisterView.as_view()),

path('tasks',TaskListCreateView.as_view()),

path('tasks/<int:pk>/',TaskDetailView.as_view()),

path('my-tasks',MyTasksView.as_view()),

path('assigned-tasks',AssignedTasksView.as_view()),

]