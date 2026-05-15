import pytest
from uuid import uuid7


@pytest.mark.katalog_02
@pytest.mark.unit
def test_add_to_favourites__success(favourites_manager):
    '''
    KATALOG-02-AC-01
    '''
    # Setup
    book_id = uuid7()

    # Exercise
    favourites_manager.add(book_id)

    # Verify
    assert book_id in favourites_manager.favourite_ids


@pytest.mark.katalog_02
@pytest.mark.unit
def test_remove_from_favourites__success(favourites_manager):
    '''
    KATALOG-03-AC-02
    '''
    # Setup: Add a book to favourites first
    book_id = uuid7()
    favourites_manager.add(book_id)
    assert book_id in favourites_manager.favourite_ids

    # Exercise
    favourites_manager.remove(book_id)

    # Verify
    assert book_id not in favourites_manager.favourite_ids
