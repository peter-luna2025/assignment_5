import pytest
from fuel import convert, gauge


# -------------------------
# Tests for convert()
# -------------------------

def test_convert_valid():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/1") == 0


def test_convert_zero_denominator():
    with pytest.raises(ValueError):
        convert("1/0")


def test_convert_negative_values():
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("1/-4")


def test_convert_non_integer():
    with pytest.raises(ValueError):
        convert("1.5/3")
    with pytest.raises(ValueError):
        convert("three/four")


def test_convert_improper_fraction():
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("10/3")


def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("1//4")
    with pytest.raises(ValueError):
        convert("14")
    with pytest.raises(ValueError):
        convert("1/2/3")


# -------------------------
# Tests for gauge()
# -------------------------

def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_middle():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
