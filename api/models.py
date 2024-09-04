from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    
    def __str__(self) -> str:
        return self.name

class Column(models.Model):
    title = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="columns")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="columns")
    
    def __str__(self) -> str:
        return self.title
    
class Todo(models.Model):
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    created_at = models.DateTimeField(auto_now_add=True)
    projectId = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="todos", default=1)
    column  = models.CharField(max_length=20, default="todo")
    
    def __str__(self) -> str:
        return self.description
    