from behave import given, then, when


@given(u'the user has no favourited books')
def step_user_has_no_favourited_books(context):
    context.base_page.navigate_to_self()
    context.base_page.navigate_to_favourites()


@given(u'the user has the following favourited books:')
def step_setup_favourited_books(context):
    context.base_page.navigate_to_self()
    context.base_page.navigate_to_katalog()

    # We will store the favourited books in the context object, so that we can check them later in the test.
    context.favourited_books = []

    for row in context.table:
        title = row['title']
        # Manually favouruite the book by clicking the heart button
        context.katalog_page.toggle_favourite(title=title, initial_heart_state="empty")
        context.favourited_books.append(title)


@when(u'the user is on the "Favourites" page')
def step_navigate_to_favourites_page(context):
    context.base_page.navigate_to_favourites()


@then(u'a message should be shown indicating the purpose of the page')
def step_check_favourites_page_empty_message(context):
    assert context.favourites_page.no_favourites_text_visible(), "Expected empty message not found"


@then(u'the page should display a list of only the favourited books')
def check_favourited_books_list(context):
    for title in context.favourited_books:
        expected_status = "present"
        actual_status = context.favourites_page.is_book_in_list(title)
        assert actual_status == expected_status, f"Expected book '{title}' to be '{expected_status}' on the Favourites page, but it was '{actual_status}'"

    num_books_in_list = context.favourites_page.get_favourite_count()
    num_added_favs = len(context.favourited_books)
    assert num_books_in_list == num_added_favs, f"Expected {num_added_favs} favourites, got {num_books_in_list}"
