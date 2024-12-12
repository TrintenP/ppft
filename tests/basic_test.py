"""Placeholder for testing GitHub Actions"""

from ppft.util import entrypoints


def test_basic():
    """Ensure ppft is in context"""
    assert entrypoints.return_true()
