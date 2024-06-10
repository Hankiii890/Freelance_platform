from django.db import models
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


class SMSMessage(models.Model):
    send_message = models.CharField(max_length=55)     # Откого смс
    executor = models.ForeignKey(Executor, on_delete=models.CASCADE)     # Связь с исполнителем
    message = models.CharField(max_length=255)
    send_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.send_message} -> {self.executor} ({self.send_at})'

