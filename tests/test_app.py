"""Tests for app.py"""

from app import add, is_even, reverse_string, multiply


class TestMaths:
    """Tests for maths functions."""

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(9, 9) == 81

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, 3) == -6

    def test_add_negative(self):
        """Test adding negative numbers."""
        assert add(-1, -1) == -2

    def test_add_positive(self):
        """Test adding positive numbers."""
        assert add(4, 3) == 7

    def test_multiply_zero(self):
        """Test zero multiplication."""
        assert multiply(0, 5) == 0

    def test_multiply_two_negatives(self):
        """Test multiplying two negative numbers."""
        assert multiply(-2, -2) == 4


class TestStrings:
    """Tests for string functions."""

    def test_reverse(self):
        assert reverse_string("hello") == "olleh"

    def test_is_even(self):
        assert is_even(4) is True
        assert is_even(3) is False