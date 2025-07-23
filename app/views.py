from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import  Producto
from django.urls import reverse_lazy

class ProductoListView(ListView):
    model = Producto
    template_name = 'app/lista.html'

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'unidades','precio','categoria']
    template_name = 'app/formulario.html'
    success_url = reverse_lazy('lista_productos')


class ProductoUpdateView(UpdateView, LoginRequiredMixin):
    model = Producto
    fields = ['nombre', 'unidades','precio','categoria']
    template_name = 'app/formulario.html'
    success_url = reverse_lazy('lista_productos')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'app/eliminar.html'
    success_url = reverse_lazy('lista_productos')