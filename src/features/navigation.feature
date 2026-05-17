Feature: Main Navigation
  As a user
  I want to use the main navigation menu
  So that I can switch between different views of the application

  @nav_01
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