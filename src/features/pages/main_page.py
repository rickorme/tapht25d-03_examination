
class MainPage:
    def __init__(self, base_url, page):
        self.base_url = base_url
        self.page = page

    # more methods as we go

    def navigate(self):
        self.page.goto(self.base_url, timeout=5000)
