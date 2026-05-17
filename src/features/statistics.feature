Feature: Statistics Tracking
  As a user 
  I want the Statistik page to update dynamically
  So that I always see the accurate count of total books and favourites

  @stat_01
  Scenario: Favourites count updates when books are favourited and unfavourited
    # 1. Initial State Check
    Given the user is on the "Statistics" page
    Then the total count of books should be 13
    And the count of favourites should be 0

    # 2. Add a favourite and verify the state updated
    When the user navigates to the "Katalog" page
    And the user favourites the book "The Bugs are Coming"
    And the user navigates to the "Statistics" page
    Then the total count of books should be 13
    And the count of favourites should be 1

    # 3. Remove the favourite and verify the state reverted
    When the user navigates to the "Katalog" page
    And the user unfavourites the book "The Bugs are Coming"
    And the user navigates to the "Statistics" page
    Then the total count of books should be 13
    And the count of favourites should be 0

  @stat_01
  Scenario: Total book count updates when a new book is added
    Given the user is on the "Statistics" page
    Then the total count of books should be 13

    When the user navigates to the "Add Book" page
    And the user adds a new book titled "Playwright for Beginners" by "Test Author"
    And the user navigates to the "Statistics" page
    Then the total count of books should be 14