from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from .models import SMSMessage

from .models import Executor


def index(request):
    return render(request, 'cabinets/index.html')


class ExecutorListView(generic.ListView):
    """
    Отображение списка объектов модели Executor
    """
    model = Executor    # Указывам с какой моделью работаем
    queryset = Executor.objects.all()   #  Задаем запрос к базе данных, чтобы получить все объекты модели
    template_name = 'cabinets/executor_cabinet.html'    # Шаблон, отображения списков объекта


class ExecutorDetailView(generic.DetailView):
    """
    Детальная информации об одном объекте модели
    """
    model = Executor
    template_name = 'cabinets/executor_detail.html'
    pk_url_kwarg = 'pk'     # Фильтруем по первичному ключу

    def get_queryset(self):
        """
        Возвращаем только объект Executor с идентификатором, указанным в параметрах URL
        """
        return Executor.objects.filter(pk=self.kwargs['pk'])


def write_message(request, executor_id):
    '''Обрабатываем отправку СМС'''
    if request.method == 'POST':
        executor_id = request.POST.get('executor_id')
        sender_name = request.POST.get('sender_name')
        message = request.POST.get('message')

        executor = Executor.objects.get(pk=executor_id)
        sms = SMSMessage(sender_name=sender_name, executor=executor, message=message)
        sms.save()

    return redirect('executor_detail', pk=executor_id)