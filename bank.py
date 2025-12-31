import pytest
from plates import is_valid


def test_valid_length():
    assert is_valid("AB123") is True
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False


def test_first_two_letters():
    assert is_valid("AB123") is True


def test_only_letters_and_digits():
    assert is_valid("AB123") is True
    assert is_valid("AB-123") is False
    assert is_valid("AB 123") is False


def test_digits_following_letters():
    assert is_valid("AB123") is True


def test_no_leading_zero_in_numbers():
    assert is_valid("AB012") is False
    assert is_valid("AB102") is True
