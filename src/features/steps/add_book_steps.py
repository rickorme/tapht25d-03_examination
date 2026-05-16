from behave import given, then, when


@given(u'the user is on the "Add Book" page')
def step_navigate_to_add_book_page(context):
    context.base_page.navigate_to_self()
    context.base_page.navigate_to_add_book()


@when(u'the user enters "{title}" into the "Title" field')
def enter_title(context, title):
    context.add_book_page.enter_title(title)


@when(u'the user enters "{author}" into the "Author" field')
def enter_author(context, author):
    context.add_book_page.enter_author(author)


@when(u'the user clicks the "Add New Book" button')
def click_add_book_button(context):
    context.add_book_page.click_add_book_button()


@then(u'the "Add New Book" button should be "{expected_state}"')
def check_add_book_button_state(context, expected_state):
    actual_state = context.add_book_page.get_add_book_button_state()
    assert actual_state == expected_state, f"Expected 'Add New Book' button to be '{expected_state}', but it was '{actual_state}'"


@then(u'the catalogue should display the new book "{title}" by "{author}"')
def check_book_in_catalogue(context, title, author):
    context.base_page.navigate_to_katalog()
    all_books = context.katalog_page.get_books()

    book_found = False
    for i in range(all_books.count()):
        current_book = all_books.nth(i)
        full_text = current_book.inner_text()
        clean_text = full_text.replace("❤️", "").strip()

        if f'"{title}", {author}' == clean_text:
            book_found = True
            break

    assert book_found, f"Book '{title}' by '{author}' was not found in the catalogue"


@then(u'the new book "{title}" by "{author}" should not be marked as a favourite')
def check_book_not_favourite(context, title, author):

    # First check the state of the favourite button on the Katalog page
    context.base_page.navigate_to_katalog()
    fav_btn = context.katalog_page.get_fav_btn_by_title(title)
    fav_btn_state = context.katalog_page.current_fav_btn_state(fav_btn)
    assert fav_btn_state == "empty", f"Expected heart button for book '{title}' to be 'empty', but it was '{fav_btn_state}'"

    # Next check that the book is not in the list of favourites on the Favourites page
    context.base_page.navigate_to_favourites()
    present_in_favourites = context.favourites_page.is_book_in_list(title)
    assert present_in_favourites == "notpresent", f"Expected book '{title}' to not be present on the Favourites page, but it was found there"
