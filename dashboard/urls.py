from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('init/', views.init, name='dashboard-init'),
    path('list/', views.list, name='dashboard-list'),
    path('planesvendidos/', views.planes_vendidos, name='planes-vendidos'),
    path('agencias/', views.agencias, name='agencias'),
    path('agencia/<int:pk>/planesvendidos/', views.agencia_planes_vendidos, name='agencia-planes-vendidos'),
]