from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('categorias/<int:id>', views.categoria, name='categoria'),
]