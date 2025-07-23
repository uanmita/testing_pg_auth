import pytest
from django.urls import reverse

@pytest.mark.django_db

def test_ProductoListView(client, django_user_model):
    response = client.get(reverse('lista_productos'))
    assert response.status_code == 200
    assert "Title" in response.content.decode()