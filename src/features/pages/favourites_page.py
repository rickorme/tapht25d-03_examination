class FavouritesPage():

    def __init__(self, page):
        self.page = page

    def is_book_in_list(self, title):
        book_locator = self.page.get_by_test_id(f"fav-{title}")
        if book_locator.is_visible():
            return "present"
        else:
            return "notpresent"
