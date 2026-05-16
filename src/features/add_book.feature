Feature: Add New Book
  As a user
  I want to add a new book to the catalogue
  So that it is added to the system

  @addbok_01
  # ADDBOK-01-AC-01: The Add New Book button is inactive if either Title or Author are empty
  # ADDBOK-01-AC-02: The Add New Book button is active when both Title and Author are not empty
  # ADDBOK-01-AC-05: It is not possible to add a book without a title
  # ADDBOK-01-AC-06: It is not possible to add a book without an author
  Scenario Outline: Add New Book button state validation
    Given the user is on the "Add Book" page
    When the user enters "<title>" into the "Title" field
    And the user enters "<author>" into the "Author" field
    Then the "Add New Book" button should be "<expected_state>"

    Examples:
      | title      | author         | expected_state |
      | The Hobbit | J.R.R. Tolkien | enabled         |
      | <empty>    | J.R.R. Tolkien | disabled       |
      | The Hobbit | <empty>        | disabled       |
      | <empty>    | <empty>        | disabled       |

  @addbok_01
  # ADDBOK-01-AC-03: When a book is added, it appears in the catalogue
  # ADDBOK-01-AC-04: A newly added book is not marked as a favourite
  Scenario Outline: Successfully adding a new book
    Given the user is on the "Add Book" page
    When the user enters "<title>" into the "Title" field
    And the user enters "<author>" into the "Author" field
    And the user clicks the "Add New Book" button
    Then the catalogue should display the new book "<title>" by "<author>"
    Then the new book "<title>" by "<author>" should not be marked as a favourite

    Examples:
      | title                                        | author      |
      | 127.0.0.1 is where the heart is              | Ella Wurld  |
      | Surviving "Quick Fixes", that last for years | Harry Hack  |