from rest_framework.routers import DefaultRouter
from django.urls import path

#from todolist_core.todolist import urlpatterns
from .views import TodolistViewSet, CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView

app_name = 'tasks'

router = DefaultRouter()
router.register('tasks', TodolistViewSet )

urlpatterns = [
    path('comments/', CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view())
] + router.urls