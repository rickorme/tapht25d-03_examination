import re


class StatisticsPage():

    def __init__(self, page):
        self.page = page

    def find_integer_in_string(self, text_string):
        # Use Regex to find the first sequence of digits (\d+) in the string
        match = re.search(r'\d+', text_string)
        if match:
            # 4. Convert the matched string ("13") into an integer (13) and return it
            return int(match.group())
        else:
            # Helpful error message if the UI changes completely
            raise ValueError(f"Could not find a number in the text: '{text_string}'")

    def get_total_books(self):
        count_locator = self.page.get_by_test_id("book-count")
        full_text = count_locator.inner_text()
        count = self.find_integer_in_string(full_text)
        return count

    def get_favourite_stats_count(self):
        count_locator = self.page.get_by_test_id("stars-count")
        full_text = count_locator.inner_text()
        count = self.find_integer_in_string(full_text)
        return count
