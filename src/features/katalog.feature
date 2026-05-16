Feature: Book Catalogue
  As a user
  I want to view and manage books in the catalogue
  So that I can find new books and track my favourites

  @katalog_01
  # KATALOG-01-AC-01: The Katalog page shows all 13 books.
  # KATALOG-01-AC-02: Every book displays a heart button
  # KATALOG-01-AC-03: Every book is displayed with it's title and author
  Scenario: Viewing the initial catalogue
    Given the user is on the "Katalog" page
    Then the catalogue should display 13 books
    And every book should display a title, an author, and a heart button

  @katalog_02 @katalog_03
  # KATALOG-02-AC-01: Clicking an empty heart beside a book changes the state of the heart to filled.
  # KATALOG-02-AC-02: The favourited book appears in the list of favourites
  # KATALOG-03-AC-01: Clicking an filled heart beside a book changes the state of the heart to empty.
  # KATALOG-03-AC-02: The un-favourited book is removed from the list of favourites
  Scenario Outline: Toggling a book's favourite status
    Given the user is on the "Katalog" page
    When the user clicks the heart button with an intial state of "<initial_heart_state>" for the book "<title>"
    Then the heart button for "<title>" should be "<new_heart_state>"
    Then "<title>" should be "<expected_status>" on the "Favourites" page

    Examples:
      | initial_heart_state | new_heart_state | expected_status  | title                                   | 
      | empty               | filled          | present          | Ormar på ett plan: En Python-berättelse |
      | filled              | empty           | notpresent       | Ormar på ett plan: En Python-berättelse |
      | filled              | empty           | notpresent       | Python för folk som hatar ormar         |
      | empty               | filled          | present          | The Bugs are Coming                     |
      | filled              | empty           | notpresent       | The Bugs are Coming                     |
