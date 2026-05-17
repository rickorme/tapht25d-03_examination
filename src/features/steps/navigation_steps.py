# tests/e2e/steps/navigation_steps.py
from behave import then


# Map plain English names to the exact data-testids in the DOM
PAGE_TO_TEST_ID = {
    "Katalog": "catalog",
    "Add Book": "add-book",
    "Favourites": "favorites",
    "Statistics": "statistics"
}


@then('the navigation button for "{page_name}" should be disabled')
def step_verify_active_button_disabled(context, page_name):
    # 1. Store the active page in context so the NEXT step knows what to ignore
    context.active_nav_page = page_name

    # 2. Get the test ID from our dictionary
    test_id = PAGE_TO_TEST_ID[page_name]

    # 3. Locate the button and assert it is disabled
    button = context.base_page.page.get_by_test_id(test_id)
    assert button.is_disabled(), f"Expected the '{page_name}' button to be disabled because it is the active page, but it was enabled."


@then('the navigation buttons for all other pages should be enabled')
def step_verify_other_buttons_enabled(context):
    # 1. Retrieve the active page we saved in the previous step
    active_page = getattr(context, 'active_nav_page', None)
    assert active_page is not None, "Active page was not set. Ensure the 'button should be disabled' step runs first."

    # 2. Loop through all the buttons in our dictionary
    for page_name, test_id in PAGE_TO_TEST_ID.items():

        # 3. If it is NOT the active page, assert that it IS enabled
        if page_name != active_page:
            button = context.base_page.page.get_by_test_id(test_id)
            assert button.is_enabled(), f"Expected the '{page_name}' button to be enabled, but it was disabled."
