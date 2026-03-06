from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Task
from .serializers import RegisterSerializer,TaskSerializer
from .permissions import IsCreatorOrAssigned
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication



class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class TaskListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = [DjangoFilterBackend,SearchFilter]

    filterset_fields = ['status','priority']

    search_fields = ['title','description']

    def perform_create(self,serializer):

        serializer.save(created_by=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsCreatorOrAssigned]

class MyTasksView(APIView):

    def get(self,request):

        tasks = Task.objects.filter(created_by=request.user)

        serializer = TaskSerializer(tasks,many=True)

        return Response(serializer.data)
    
class AssignedTasksView(APIView):

    def get(self,request):

        tasks = Task.objects.filter(assigned_to=request.user)

        serializer = TaskSerializer(tasks,many=True)

        return Response(serializer.data)