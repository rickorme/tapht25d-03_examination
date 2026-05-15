# test_integration.py
import pytest


@pytest.mark.addbok_01
@pytest.mark.integration
def test_new_book_is_not_favourited(catalogue):
    '''
    ADDBOK-01-AC-04:
    A newly added book is not marked as a favourite
    '''
    # Add the book via the BookStore (catalogue)
    new_book = catalogue.add_book(title="The Hobbit", author="J.R.R. Tolkien")

    # Assert the state in the FavouriteBooks manager
    assert catalogue.favourites_manager.is_favourite(new_book.id) is False
    assert not new_book.favourite


@pytest.mark.katalog_02
@pytest.mark.katalog_03
@pytest.mark.integration
def test_toggle_favourite__favourited_book_is_added_to_favourites(catalogue):
    '''
    KATALOG-02-AC-02:
    The favourited book appears in the list of favourites
    '''
    # Add a book to the catalogue
    new_book = catalogue.add_book(title="1984", author="George Orwell")

    # Toggle it as a favourite
    new_book = catalogue.toggle_favourite(new_book.id)

    # Assert it's now in the favourites list
    assert new_book.id in catalogue.favourites_manager.favourite_ids
    assert catalogue.favourites_manager.is_favourite(new_book.id) is True
    assert new_book.favourite


@pytest.mark.katalog_02
@pytest.mark.katalog_03
@pytest.mark.integration
def test_toggle_favourite__unfavourited_book_is_removed_from_favourites(catalogue):
    '''
    KATALOG-02-AC-02:
    The favourited book appears in the list of favourites
    KATALOG-03-AC-02:
    The un-favourited book is removed from the list of favourites
    '''
    # Add a book to the catalogue
    new_book = catalogue.add_book(title="1984", author="George Orwell")

    # Toggle it as a favourite
    new_book = catalogue.toggle_favourite(new_book.id)

    # Assert it's now in the favourites list
    assert new_book.id in catalogue.favourites_manager.favourite_ids
    assert catalogue.favourites_manager.is_favourite(new_book.id) is True
    assert new_book.favourite

    # Toggle it again to remove from favourites
    new_book = catalogue.toggle_favourite(new_book.id)

    # Assert it has been removed from the favourites list
    assert new_book.id not in catalogue.favourites_manager.favourite_ids
    assert catalogue.favourites_manager.is_favourite(new_book.id) is False
    assert not new_book.favourite
