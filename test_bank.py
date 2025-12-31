import pytest
from bank import get_value


def test_hello_variants():
    assert get_value("hello") == "$0"
    assert get_value("Hello") == "$0"
    assert get_value("hello,") == "$0"
    assert get_value("hello there") == "$0"
    assert get_value("Hello, Newman") == "$0"


def test_whats_happening():
    assert get_value("What's happening?") == "$100"


def test_everything_else_is_20():
    assert get_value("hey") == "$20"
    assert get_value("hi") == "$20"
    assert get_value("yo") == "$20"
    assert get_value("sup") == "$20"
    assert get_value("good morning") == "$20"
    assert get_value("h") == "$20"
    assert get_value("random text") == "$20"
