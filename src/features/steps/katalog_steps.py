from behave import given, then, when


@given(u'the user is on the "Katalog" page')
def step_navigate_to_katalog_page(context):
    context.base_page.navigate_to_self()
    context.base_page.navigate_to_katalog()
    # raise StepNotImplementedError(u'Given the user is on the "Katalog" page')


@then(u'the catalogue should display 13 books')
def step_count_displayed_books(context):
    expected_books = 13
    displayed_books = context.katalog_page.book_count()
    assert displayed_books == expected_books, f"Expected {expected_books} books, but found {displayed_books}"


@then(u'every book should display a title, an author, and a heart button')
def step_display_book_details(context):
    context.katalog_page.check_book_details()


@when(u'the user clicks the heart button with an intial state of "{initial_heart_state}" for the book "{title}"')
def step_toggle_favourite(context, title, initial_heart_state):
    context.katalog_page.toggle_favourite(title=title, initial_heart_state=initial_heart_state)


@then(u'the heart button for "{title}" should be "{new_heart_state}"')
def step_check_heart_state(context, title, new_heart_state):
    fav_btn = context.katalog_page.get_fav_btn_by_title(title)
    current_state = context.katalog_page.current_fav_btn_state(fav_btn)
    assert current_state == new_heart_state, f"Expected heart button state to be ' {new_heart_state}', but got '{current_state}' for book '{title}'"


@then(u'"{title}" should be "{expected_status}" on the "Favourites" page')
def step_check_book_status_on_mina_böcker(context, title, expected_status):
    context.base_page.navigate_to_favourites()
    actual_status = context.favourites_page.is_book_in_list(title)
    assert actual_status == expected_status, f"Expected book '{title}' to be '{expected_status}' on the Favourites page, but it was '{actual_status}'"
