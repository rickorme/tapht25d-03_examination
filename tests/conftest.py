# conftest.py
import pytest
from src.backend.book_store import BookStore


# 1. Share the catalogue fixture globally
@pytest.fixture
def catalogue():
    """Provides a fresh BookStore instance for each test."""
    return BookStore()
