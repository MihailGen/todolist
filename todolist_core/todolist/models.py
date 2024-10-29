from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=150, verbose_name='Тема задачи')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    due_date = models.DateTimeField(null=True, blank=True, verbose_name='Cроки выполнения')
    tags = models.TextField(default='задачи', verbose_name='Теги')
    author = models.CharField(max_length=50, null=True, blank=True, verbose_name='Автор')
    tags = models.ManyToManyField('Tag', related_name='tasks')
    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self):
        return self.name

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.id} on {self.created_at}'

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name