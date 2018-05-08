from model.group import Group


def test_mod_group(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_first_group(Group(name="New Name", header="Kokoko 123", footer="Tytyty 456"))
    app.session.logout()