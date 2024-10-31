from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, mixins

from .models import Task, Comment
from .serializers import TaskSerializer, CommentSerializer



def base(request):
    return render(request, 'todolist/base.html')


class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentAPIView(generics.ListAPIView, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    pass