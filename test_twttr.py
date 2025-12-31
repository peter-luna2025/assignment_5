import pytest
from twttr import shorten

def test_removes_vowels_lowercase():
    assert shorten("hello world") == "hll wrld"

def test_mixed_case():
    assert shorten("PyTest") == "PyTst"

def test_no_vowels():
    assert shorten("rhythm") == "rhythm"

def test_empty_string():
    assert shorten("") == ""
