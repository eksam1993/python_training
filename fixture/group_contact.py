
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
            wd = self.app.wd
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
            wd = self.app.wd
            self.open_groups_page()
            # init group creation
            wd.find_element_by_name("new").click()
            self.fill_group_form(group)
            # submit group creation
            wd.find_element_by_name("submit").click()
            self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def fill_first_contact(self, contacts):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contacts.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contacts.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contacts.company)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contacts.email)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submint first group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def return_to_groups_page(self):
            wd = self.app.wd
            wd.find_element_by_link_text("group page").click()

    def add_new_contact(self, contacts):
        wd = self.app.wd
        # add new contact
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contacts.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contacts.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contacts.company)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contacts.email)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submint first contact
        wd.find_element_by_name("Delete").click()
        # confirm contact removal
        wd.switch_to_alert().accept()
        self.return_to_groups_page()

    def select_first_contact(self):
        # select first contact
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def mod_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        self.return_to_groups_page()

    def mod_first_contact(self, contacts):
        wd = self.app.wd
        self.select_first_contact()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_first_contact(contacts)
        wd.find_element_by_name("update").click()




