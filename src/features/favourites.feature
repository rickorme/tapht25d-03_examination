Feature: My Favourite Books
  As a user
  I want to go to the Favourites page
  So that I can see a list of my favourite books

  @minbok_01
  # MINBOK-01-AC-01: When no books have been favourited, 
  # a message is shown indicating the purpose of the page
  Scenario: Viewing an empty favourites list
    Given the user has no favourited books
    When the user is on the "Favourites" page
    Then a message should be shown indicating the purpose of the page

  @minbok_01
  # MINBOK-01-AC-02: All favourited books appear as a list
  # MINBOK_01-AC-03: Only favourited books appear in the list
  Scenario: Viewing a populated favourites list
    Given the user has the following favourited books:
        | title                           |
        | Why Your Tests Are Lying to You |
        | The Bugs are Coming             |
    When the user is on the "Favourites" page
    Then the page should display a list of only the favourited books