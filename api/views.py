from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, TodoSerializer, ColumnSerializer, ProjectSerializer, CustomTokenObtainPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Project, Column, Todo
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
 
class CreateUserView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
class ListCreateProjectView(generics.ListCreateAPIView): # lists or create project according to the get or post request 
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(created_by=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            return serializer.save(created_by=self.request.user)
        else:
            print(serializer.error)
            
class DestroyProjectView(generics.DestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Project.objects.filter(created_by=self.request.user)
            
class ListCreateColumnView(generics.ListCreateAPIView):
    serializer_class = ColumnSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        project = self.request.query_params["projectId"] 
        user = self.request.user
        return Column.objects.filter(projectId=project, created_by=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            return serializer.save(created_by=self.request.user)
        else:
            print(serializer.error)
            
class ListCreateTodoView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        project = self.request.query_params["projectId"]
        return Todo.objects.filter(projectId=project, created_by=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            return serializer.save(created_by=self.request.user)
        else:
            print(serializer.error)

class UpdateTodoView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(created_by=user)
    
    

