from django.contrib import admin

from .models import Executor, Skill, Message

# Register your models here.


admin.site.register(Executor)
admin.site.register(Skill)
admin.site.register(Message)


