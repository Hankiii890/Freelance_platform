from django.shortcuts import render, redirect
from django.views import generic
from .models import Executor, Message
from .forms import MessageForm


def index(request):
    return render(request, 'cabinets/index.html')


class ExecutorListView(generic.ListView):
    """
    Display list models objects
    """
    model = Executor    # Указывам с какой моделью работаем
    queryset = Executor.objects.all()   #  Задаем запрос к базе данных, чтобы получить все объекты модели
    template_name = 'cabinets/executor_cabinet.html'    # Шаблон, отображения списков объекта


class ExecutorDetailView(generic.DetailView):
    """
    model object information
    """
    model = Executor
    template_name = 'cabinets/executor_detail.html'
    pk_url_kwarg = 'pk'     # Фильтруем по первичному ключу

    def get_queryset(self):
        """
        Return executor URL
        """
        return Executor.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context


class SendMessageView(generic.DetailView):

    def get_queryset(self):
        return Message.objects.all()

    def post(self, request, pk):
        model = Message
        template_name = 'cabinets/dialogue'

        executor = Executor.objects.get(pk=pk)
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.executor = executor
            message.save()
            return redirect('executor_detail', pk=pk)
        return render(request, 'cabinets/executor_detail.html', {'form': form, 'executor': executor})