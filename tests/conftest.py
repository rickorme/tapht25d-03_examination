# conftest.py
import pytest
from src.backend.the_reading_list import BookStore, FavouriteBooks


@pytest.fixture
def favourites_manager():
    """Provides a fresh FavouriteBooks instance for each test."""
    return FavouriteBooks()


# Share the catalogue fixture globally
@pytest.fixture
def catalogue(favourites_manager):
    """Provides a fresh BookStore instance for each test."""
    return BookStore(favourites_manager=favourites_manager)
