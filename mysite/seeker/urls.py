from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('executor/', views.ExecutorListView.as_view(), name='executor_cabinet'),
    path('executor/<int:pk>/', views.ExecutorDetailView.as_view(), name='executor_detail'),
    path('send_message/<int:executor_id>', views.send_message, name='send_message'),
]