from rest_framework.routers import DefaultRouter

#from todolist_core.todolist import urlpatterns
from .views import TodolistViewSet
app_name = 'tasks'

router = DefaultRouter()
router.register('tasks', TodolistViewSet )

urlpatterns = [


] + router.urls