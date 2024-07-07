from django.db import models
from django.apps import apps
from django.conf import settings
from django.utils import timezone


class Executor(models.Model):
    """Исполнитель"""
    name = models.CharField(max_length=50)
    skills = models.ManyToManyField('Skill', related_name='executors')
    experience = models.IntegerField()
    education = models.TextField()
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=255, unique=True)


class Skill(models.Model):
    """Навыки"""
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class Message(models.Model):
    """ Model for message between executor and user  """

    executor = models.ForeignKey('Executor', on_delete=models.CASCADE, related_name='messages')     # Можем получить список всех сообщение исполнителя с помощью: executor.messages
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Проверка {self.executor}'  # Не работает
