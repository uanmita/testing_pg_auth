from django.urls import path
from . import views

urlpatterns = [
path('', views.ProductoListView.as_view(), name='lista_productos'),
path('categorias/', views.CategoriaListView.as_view(), name='lista_categorias'),
path('categorias/nueva/', views.CategoriaCreateView.as_view(), name='crear_categoria'),
path('categorias/editar/<int:pk>/', views.CategoriaUpdateView.as_view(), name='editar_categoria'),
path('categorias/eliminar/<int:pk>/', views.CategoriaDeleteView.as_view(), name='eliminar_categoria'),
path('nuevo/', views.ProductoCreateView.as_view(), name='crear_producto'),
path('editar/<int:pk>/', views.ProductoUpdateView.as_view(), name='editar_producto'),
path('eliminar/<int:pk>/', views.ProductoDeleteView.as_view(), name='eliminar_producto'),
]