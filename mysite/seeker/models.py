from django.db import models


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


