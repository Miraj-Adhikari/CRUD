from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_client/<int:client_id>/', views.delete_client, name='delete_client'),
    path('update_client/<int:client_id>/', views.update_client, name='update_client'),
]
