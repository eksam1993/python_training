# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_contacts(app):
        app.group.add_new_contact(Contacts(firstname="Ekaterina", lastname="Samoilova", nickname="eksam", title="123", company="Ek and Co", email="esamoilova@mail.ru"))


def test_add_two_contacts(app):
        app.group.add_new_contact(Contacts(firstname="Ivan", lastname="Petrov", nickname="ivaN", title="luxry", company="VIPcomp", email="VIOiva123@mail.ru"))
