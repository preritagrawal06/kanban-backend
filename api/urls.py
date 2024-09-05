from django.urls import path
from .views import ListCreateColumnView, ListCreateProjectView, ListCreateTodoView, UpdateTodoView, DestroyProjectView

urlpatterns = [
    path("project/", ListCreateProjectView.as_view()),
    path("project/<int:pk>", DestroyProjectView.as_view()),
    path("column/", ListCreateColumnView.as_view()),
    path("todo/", ListCreateTodoView.as_view()),
    path("todo/<int:pk>", UpdateTodoView.as_view())
]
