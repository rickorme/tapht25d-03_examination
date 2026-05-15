import pytest

from src.backend.the_reading_list import BookStore


@pytest.mark.addbok_01
@pytest.mark.unit
def test_add_book__success(catalogue):
    '''
    ADDBOK-01-AC-03
    '''
    new_title = "Book Title"
    new_author = "Author Name"
    new_book = catalogue.add_book(title=new_title, author=new_author)

    assert new_book is not None
    assert new_book.title == new_title
    assert new_book.author == new_author

    books = catalogue.get_books()
    assert len(books) == 1
    assert books[0].title == new_title
    assert books[0].author == new_author


@pytest.mark.addbok_01
@pytest.mark.unit
def test_add_book__no_title(catalogue):
    '''
    ADDBOK-01-AC-05:
    Verify that an error is raised when trying to add a book without a title
    '''
    with pytest.raises(ValueError, match="Title is required"):
        new_title = ""
        new_author = "Author Name"
        new_book = catalogue.add_book(title=new_title, author=new_author)
        assert new_book is None


@pytest.mark.addbok_01
@pytest.mark.unit
def test_add_book__no_author(catalogue):
    '''
    ADDBOK-01-AC-06:
    Verify that an error is raised when trying to add a book without an author
    '''
    with pytest.raises(ValueError, match="Author is required"):
        new_title = "Book Title"
        new_author = ""
        new_book = catalogue.add_book(title=new_title, author=new_author)
        assert new_book is None


@pytest.mark.addbok_01
@pytest.mark.unit
def test_add_book__long_title(catalogue):
    '''
    ADDBOK-01-AC-07:
    Verify that an error is raised when trying to add a book with a title that is too long
    '''
    with pytest.raises(
            ValueError,
            match=f"Title must be at most {catalogue.max_title_length} characters long"
            ):
        long_title = "A" * (catalogue.max_title_length + 1)
        new_author = "Author Name"
        new_book = catalogue.add_book(title=long_title, author=new_author)
        assert new_book is None


@pytest.mark.addbok_01
@pytest.mark.unit
def test_add_book__long_author(catalogue):
    '''
    ADDBOK-01-AC-08:
    Verify that an error is raised when trying to add a book with an author name that is too long
    '''
    with pytest.raises(
            ValueError,
            match=f"Author must be at most {catalogue.max_author_length} characters long"
            ):
        new_title = "Book Title"
        long_author = "B" * (catalogue.max_author_length + 1)
        new_book = catalogue.add_book(title=new_title, author=long_author)
        assert new_book is None


@pytest.mark.addbok_01
@pytest.mark.unit
def test_add_book__new_book_gets_unique_id(catalogue):
    '''
    ADDBOK-01-AC-09
    '''
    new_title1 = "Book Title 1"
    new_author1 = "Author Name 1"
    book1 = catalogue.add_book(title=new_title1, author=new_author1)

    new_title2 = "Book Title 2"
    new_author2 = "Author Name 2"
    book2 = catalogue.add_book(title=new_title2, author=new_author2)

    assert book1.id is not None
    assert book2.id is not None
    assert book1.id != book2.id


@pytest.mark.katalog_02
@pytest.mark.unit
def test_toggle_favourite__calls_add_when_not_favourited(mocker):
    '''
    KATALOG-02-AC-02
    '''
    # 1. ARRANGE: Create a mock manager
    mock_manager = mocker.MagicMock()
    # Program the mock to say "No, this book is not a favourite yet"
    mock_manager.is_favourite.return_value = False

    # Inject the mock into a real BookStore
    catalogue = BookStore(favourites_manager=mock_manager)
    book = catalogue.add_book(title="Dune", author="Frank Herbert")

    # 2. ACT
    catalogue.toggle_favourite(book.id)

    # 3. ASSERT
    # Prove the BookStore correctly told the manager to add the book
    mock_manager.add.assert_called_once_with(book.id)
    mock_manager.remove.assert_not_called()


@pytest.mark.katalog_03
@pytest.mark.unit
def test_toggle_favourite__calls_remove_when_already_favourited(mocker):
    '''
    KATALOG-03-AC-02
    '''
    # 1. ARRANGE: Create a mock manager
    mock_manager = mocker.MagicMock()
    # Program the mock to say "This book is already a favourite"
    mock_manager.is_favourite.return_value = True

    catalogue = BookStore(favourites_manager=mock_manager)
    book = catalogue.add_book(title="Dune", author="Frank Herbert")

    # 2. ACT
    catalogue.toggle_favourite(book.id)

    # 3. ASSERT
    # Prove the BookStore correctly told the manager to remove the book
    mock_manager.remove.assert_called_once_with(book.id)
    mock_manager.add.assert_not_called()
