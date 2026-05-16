import re


class KatalogPage():

    def __init__(self, page):
        self.page = page

    def book_count(self):
        return self.page.locator(".book").count()

    def get_books(self):
        return self.page.locator(".book")

    def check_book_details(self):
        all_books = self.get_books()

        for i in range(all_books.count()):
            current_book = all_books.nth(i)
            heart_button = current_book.locator('.star[role="button"]')
            assert heart_button.is_visible(), f"Heart button missing on book at index {i}"

            full_text = current_book.inner_text()
            clean_text = full_text.replace("❤️", "").strip()
            print(clean_text)

            # The regex pattern checks for a format like: "Book Title", Author Name
            regex_pattern = r"^\".{1,150}(\",)\s*.{1,100}$"
            assert re.compile(regex_pattern).match(clean_text), f"Title and Author not found at index {i}: {clean_text}"

    def get_fav_btn_by_title(self, title):
        return self.page.get_by_test_id(f"star-{title}")

    def current_fav_btn_state(self, button):
        # 1. Get the full class string (e.g., "star selected")
        class_attr = button.get_attribute("class")

        # 2. Check if "selected" is in that string.
        # (We also check if class_attr is not None, just to be safe!)
        if class_attr and "selected" in class_attr:
            return "filled"
        else:
            return "empty"

    def toggle_favourite(self, title, initial_heart_state):
        fav_btn = self.get_fav_btn_by_title(title)
        current_state = self.current_fav_btn_state(fav_btn)
        if current_state != initial_heart_state:
            fav_btn.click(timeout=500)

        current_state = self.current_fav_btn_state(fav_btn)
        assert current_state == initial_heart_state, f"Heart button state did not toggle as expected for book '{title}'. Expected: {initial_heart_state}, but got: {current_state}"

        fav_btn.click(timeout=500)
