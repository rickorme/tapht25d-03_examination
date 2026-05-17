Feature: Main Navigation
  As a user
  I want to use the main navigation menu
  So that I can switch between different views of the application

  @nav_01
  # NAV-01-AC-01: Clicking a navigation button switches the view to the corresponding page.
  # NAV-01-AC-02: The navigation button for the currently active page is disabled.
  # NAV-01-AC-03: The navigation buttons for all non-active pages remain enabled.
  Scenario Outline: Navigation buttons update their state based on the active view
    # Assuming the app always loads on the Katalog page by default
    Given the user is on the "Katalog" page
    When the user navigates to the "<target_page>" page
    Then the navigation button for "<target_page>" should be disabled
    And the navigation buttons for all other pages should be enabled

    Examples:
      | target_page |
      | Katalog     |
      | Add Book    |
      | Favourites  |
      | Statistics  |