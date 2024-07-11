from django.db import models
from django.apps import apps
from django.conf import settings
from django.utils import timezone


class Executor(models.Model):
    """Исполнитель"""
    name = models.CharField(max_length=50, verbose_name='Имя')
    skills = models.ManyToManyField('Skill', related_name='executors', verbose_name='Навыки')
    experience = models.IntegerField(verbose_name='Опыт')
    education = models.TextField(verbose_name='Образование')
    phone = models.CharField(blank=True, verbose_name='Телефон')
    email = models.EmailField(unique=True, verbose_name='Email')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

class Skill(models.Model):
    """Навыки"""
    description = models.CharField(max_length=255, verbose_name='Описание')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

class Message(models.Model):
    """ Model for message between executor and user  """

    executor = models.ForeignKey('Executor', on_delete=models.CASCADE, related_name='messages', verbose_name='Исполнитель')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'