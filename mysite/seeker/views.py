from django.shortcuts import render, redirect
from django.views import generic
from.models import Executor, Message
from.forms import MessageForm


def index(request):
    return render(request, 'cabinets/index.html')


class ExecutorListView(generic.ListView):
    model = Executor
    queryset = Executor.objects.all()
    template_name = 'cabinets/executor_cabinet.html'


class ExecutorDetailView(generic.DetailView):
    model = Executor
    template_name = 'cabinets/executor_detail.html'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return Executor.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context


class SendMessageView(generic.View):
    template_name = 'cabinets/dialogue.html'

    def get(self, request, pk):
        executor = Executor.objects.get(pk=pk)
        form = MessageForm()
        return render(request, self.template_name, {'form': form, 'executor': executor})

    def post(self, request, pk):
        executor = Executor.objects.get(pk=pk)
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.executor = executor
            message.save()
            return redirect('executor_detail', pk=pk)
        return render(request, self.template_name, {'form': form, 'executor': executor})