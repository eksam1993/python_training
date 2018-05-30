from model.group import Group


def test_mod_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_first_group(Group(name="New Name"))
    app.session.logout()


def test_mod_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_first_group(Group(header="New header"))
    app.session.logout()
