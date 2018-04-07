from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('init/', views.init, name='dashboard-init'),
    path('list/', views.list, name='dashboard-list'),
]