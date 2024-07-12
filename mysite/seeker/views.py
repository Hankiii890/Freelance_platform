from django.shortcuts import render, redirect
from django.views import generic
from .models import Executor
from .forms import MessageForm


def index(request):
    """Функция представления главной страницы"""
    return render(request, 'cabinets/index.html')


class ExecutorListView(generic.ListView):
    """Отображение списка всех пользователей в системе"""
    model = Executor
    queryset = Executor.objects.all()  # Отображение набора объектов для Исполнителей
    template_name = 'cabinets/executor_cabinet.html'


class ExecutorDetailView(generic.DetailView):
    """Отображение детального представления исполнителя"""
    model = Executor
    template_name = 'cabinets/executor_detail.html'
    pk_url_kwarg = 'pk'  # Аргумент ключевого слова URL для передачи первичного ключа

    def get_queryset(self):
        """Фильтрация объектов по первичному ключу"""
        return Executor.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Добавляем экземпляр MessageForm, который передадим в шаблон"""
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context


class SendMessageView(generic.View):
    """Класс обработки отправления сообщений"""
    template_name = 'cabinets/dialogue.html'

    def get(self, request, pk):
        """Отображение формы отправки сообщения при посещении пользователем URL."""
        executor = Executor.objects.get(pk=pk)
        form = MessageForm()
        return render(request, self.template_name, {'form': form, 'executor': executor})

    def post(self, request, pk):
        """Отвечает за обработку отправки формы"""
        executor = Executor.objects.get(pk=pk)
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.executor = executor
            message.save()
            return redirect('executor_detail', pk=pk)
        return render(request, self.template_name, {'form': form, 'executor': executor})