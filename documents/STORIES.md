# User Stories for Läslistan application

## Katalog Page (KATALOG)

### KATALOG-01-US
    As a user
    I want to be able to see all of the books in the catalogue
    So that I can find new books to read

#### Acceptance Criteria

- >KATALOG-01-AC-01: The Katalog page shows all 13 books.
- >KATALOG-01-AC-02: Every book displays a heart button
- >KATALOG-01-AC-03: Every book is displayed with it's title and author

### KATALOG-02-US
    As a user
    I want to be able to be able to favourite a book from the catalogue
    So that it is wasy to see in the catalogue, and it is saved to my list of favourite books

#### Acceptance Criteria

- >KATALOG-02-AC-01: Clicking an empty heart beside a book changes the state of the heart to filled.
- >KATALOG-02-AC-02: The favourited book appears in the list of favourites     

### KATALOG-03-US
    As a user
    I want to be able to be able to unfavourite a book from the catalogue
    So that it is removed from my list of favourite books

#### Acceptance Criteria

- >KATALOG-03-AC-01: Clicking an filled heart beside a book changes the state of the heart to empty.
- >KATALOG-03-AC-02: The un-favourited book is removed from the list of favourites

---

## Lägg till bok Page (ADDBOK)

### ADDBOK-01-US
    As a user
    I want to be able to add a new book, including the details: "title" and "author"
    So that it is added to the catalogue

#### Acceptance Criteria

- >ADDBOK-01-AC-01: The Add New Book button is inactive if either Title or Author are empty
- >ADDBOK-01-AC-02: The Add New Book button is active when both Title and Author are not empty
- >ADDBOK-01-AC-03: When a book is added, it appears in the catalogue
- >ADDBOK-01-AC-04: A newly added book is not marked as a favourite
- >ADDBOK-01-AC-05: It is not possible to add a book without a title
- >ADDBOK-01-AC-06: It is not possible to add a book without an author
- >ADDBOK-01-AC-07: Book title length must be less than or equal to 150 characters
- >ADDBOK-01-AC-08: Author length must be less than or equal to 100 characters
- >ADDBOK-01-AC-09: Newly added books are assigned a unique ID

---
## Mina Böcker Page (MINBOK)

### MINBOK-01-US
    As a user
    I want to go to the Mina Böcker page
    So that I can see a list of my favourite books

#### Acceptance Criteria

- >MINBOK-01-AC-01: When no books have been favourited, a message is shown indicating the purpose of the page
- >MINBOK-01-AC-02: All favourited books appear as a list 
- >MINBOK_01-AC-03: Only favourited books appear in the list

---
## Statistik Page (STAT)

### STAT-01-US
    As a user 
    I want to go to the Statistik page
    So that I can see the total number of books in the catalogue and the number of books which have been added to my favourites

#### Acceptance Criteria

- >STAT-01-AC-01: The count of books represents the total number of books on the catalogue, the initial value is 13
- >STAT-01-AC-01: The count of favourites represents the total number of favourited books in the catalogue, the initial value is 0