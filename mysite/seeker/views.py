from django.shortcuts import render
from django.views import generic

from .models import Customer,Executor


def index(request):
    return render(request, 'cabinets/index.html')


class CustomerListView(generic.ListView):
    model = Customer
    queryset = Customer.objects.all()
    template_name = 'cabinets/customer_cabinet.html'


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