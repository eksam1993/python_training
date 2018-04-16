# -*- coding: utf-8 -*-
import pytest
from model.conacts import Contacts
from fixture.application2 import Application2


@pytest.fixture
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contacts(app):
        app.login(user="admin", password="secret")
        app.add_new_contact(Contacts(firstname="Ekaterina", lastname="Samoilova", nickname="eksam", title="123", company="Ek and Co", email="esamoilova@mail.ru"))
        app.logout()


def test_add_two_contacts(app):
        app.login(user="admin", password="secret")
        app.add_new_contact(Contacts(firstname="Ivan", lastname="Petrov", nickname="ivaN", title="luxry", company="VIPcomp", email="VIOiva123@mail.ru"))
        app.logout()