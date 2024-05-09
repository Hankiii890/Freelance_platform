from django.contrib import admin

from .models import Customer, Executor, Skill

# Register your models here.

admin.site.register(Customer)
admin.site.register(Executor)
admin.site.register(Skill)


