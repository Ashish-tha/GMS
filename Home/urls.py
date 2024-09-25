from django.contrib import admin
from django.urls import path
from . import views   
views.payment

urlpatterns = [
    path("", views.index, name='index'),
    path("crud", views.crud, name="crud"),
    path('add',views.Add,name='add'),
    path('edit',views.Edit,name='edit'),
    path('update/<str:id>',views.Update,name='update'),
    path('delete/<str:id>',views.Delete,name='delete'),
    path('payment', views.payment, name="payment"),
]