from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.CustomerListView.as_view(), name='customer_cabinet'),
    path('executor/', views.ExecutorListView.as_view(), name='executor_cabinet'),
]