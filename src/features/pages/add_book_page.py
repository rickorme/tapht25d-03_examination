class AddBookPage():
    def __init__(self, page):
        self.page = page

    def get_actual_field_value(self, value):
        actual_value = "" if value == "<empty>" else value
        return actual_value

    def enter_title(self, title):
        title_field = self.page.get_by_test_id("add-input-title")
        actual_title = self.get_actual_field_value(title)
        title_field.fill(actual_title)

    def enter_author(self, author):
        author_field = self.page.get_by_test_id("add-input-author")
        actual_author = self.get_actual_field_value(author)
        author_field.fill(actual_author)

    def get_add_book_btn(self):
        return self.page.get_by_test_id("add-submit")

    def get_add_book_button_state(self):
        add_book_btn = self.get_add_book_btn()
        return "disabled" if add_book_btn.is_disabled() else "enabled"

    def click_add_book_button(self):
        add_book_btn = self.get_add_book_btn()
        if not add_book_btn.is_disabled():
            add_book_btn.click(timeout=500)
