from django.urls import path
from .views import ListCreateColumnView, ListCreateProjectView, ListCreateTodoView

urlpatterns = [
    path("project/", ListCreateProjectView.as_view()),
    path("column/", ListCreateColumnView.as_view()),
    path("todo/", ListCreateTodoView.as_view())
]
