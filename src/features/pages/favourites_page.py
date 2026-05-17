class FavouritesPage():

    def __init__(self, page):
        self.page = page

    def is_book_in_list(self, title):
        book_locator = self.page.get_by_test_id(f"fav-{title}")
        if book_locator.is_visible():
            return "present"
        else:
            return "notpresent"

    def no_favourites_text_visible(self):
        no_fav_text_locator = self.page.get_by_text("När du valt, kommer dina favoritböcker att visas här.")
        return no_fav_text_locator.is_visible()

    def get_favourite_count(self):
        fav_items = self.page.get_by_test_id("book-list").locator(".book")
        return fav_items.count()
