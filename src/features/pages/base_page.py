BASE_URL = "https://tap-ht25-testverktyg.github.io/exam/"


class BasePage:
    def __init__(self, page):
        self.base_url = BASE_URL
        self.page = page

    def navigate_to_self(self):
        self.page.goto(self.base_url, timeout=5000)
        # self.page.wait_for_timeout(1500)

    def navigate_by_button(self, button_test_id):
        nav_button = self.page.get_by_test_id(button_test_id)
        if not nav_button.is_disabled():
            nav_button.click(timeout=500)

    def navigate_to_katalog(self):
        nav_button_test_id = "catalog"
        self.navigate_by_button(nav_button_test_id)

    def navigate_to_addbok(self):
        nav_button_test_id = "add-book"
        self.navigate_by_button(nav_button_test_id)

    def navigate_to_favourites(self):
        nav_button_test_id = "favorites"
        self.navigate_by_button(nav_button_test_id)

    def navigate_to_statistics(self):
        nav_button_test_id = "statistics"
        self.navigate_by_button(nav_button_test_id)
