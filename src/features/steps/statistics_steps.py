from behave import given, then, when


@given(u'the user is on the "Statistics" page')
def step_navigate_to_add_book_page(context):
    context.base_page.navigate_to_self()
    context.base_page.navigate_to_statistics()


@when('the user {action} the book "{title}"')
def step_toggle_specific_book(context, action, title):
    """
    Handles both "favourites" and "unfavourites" actions.
    """
    # Determine what state we expect the heart to be in BEFORE we click it
    initial_state = "empty" if action == "favourites" else "filled"

    # Use the method you already wrote!
    context.katalog_page.toggle_favourite(title=title, initial_heart_state=initial_state)


@when('the user navigates to the "{page_name}" page')
def step_navigate_to_page(context, page_name):

    if page_name == "Katalog":
        context.base_page.navigate_to_katalog()
    elif page_name == "Statistics":
        context.base_page.navigate_to_statistics()
    elif page_name == "Add Book":
        context.base_page.navigate_to_add_book()
    elif page_name == "Favourites":
        context.base_page.navigate_to_favourites()
    else:
        raise ValueError(f"Navigation for '{page_name}' is not defined.")


@when(u'the user adds a new book titled {title} by {author}')
def add_book(context, title, author):
    context.add_book_page.enter_title(title)
    context.add_book_page.enter_author(author)
    context.add_book_page.click_add_book_button()


@then('the total count of books should be {expected_count:d}')
def step_verify_total_books(context, expected_count):
    actual_count = context.statistics_page.get_total_books()
    assert actual_count == expected_count, f"Expected {expected_count} books, but got {actual_count}"


@then('the count of favourites should be {expected_count:d}')
def step_verify_favourite_count(context, expected_count):
    actual_count = context.statistics_page.get_favourite_stats_count()
    assert actual_count == expected_count, f"Expected {expected_count} favs, but got {actual_count}"
