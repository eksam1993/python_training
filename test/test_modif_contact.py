from model.contacts import Contacts


def test_add_contacts(app):
        app.session.login(username="admin", password="secret")
        app.group.mod_first_contact(Contacts(firstname="Petr", lastname="Ivanov", nickname="petrhulk", title="BIGBOSS", company="Company The Best", email="petrhulk789@vov.vov"))
        app.session.logout()