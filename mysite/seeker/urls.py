from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('executor/', views.ExecutorListView.as_view(), name='executor_cabinet'),
]