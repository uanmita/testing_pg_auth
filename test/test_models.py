import pytest
from app.models import Categoria, Producto

@pytest.mark.django_db

def test_Producto():
    cat = Categoria.objects.create(nombre="camisas")
    pro = Producto.objects.create(nombre="camisa blanca", unidades=2, precio=10, categoria=cat)
    assert str(pro) == "camisa blanca"
    assert pro.categoria is cat