from django.urls import path
from . import views

urlpatterns = [
path('', views.ProductoListView.as_view(), name='lista_productos'),
path('nuevo/', views.ProductoCreateView.as_view(), name='crear_producto'),
path('editar/<int:pk>/', views.ProductoUpdateView.as_view(), name='editar_producto'),
path('eliminar/<int:pk>/', views.ProductoDeleteView.as_view(), name='eliminar_producto'),
]