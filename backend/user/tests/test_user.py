import pytest
from django.urls import reverse

from user.models import User


@pytest.mark.django_db
def test_my_user():
    me = User.objects.get(username='support_admin')
    assert me.is_superuser


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    assert User.objects.count() == 7


@pytest.mark.django_db
def test_unauthorized(client):
    url = reverse('users')
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_superuser_view(admin_client):
    url = reverse('users')
    response = admin_client.get(url)
    assert response.status_code == 200
