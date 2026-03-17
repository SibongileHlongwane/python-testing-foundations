import pytest
from app.string_utils import to_uppercase, reverse_string


@pytest.mark.parametrize("input_text, expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
    ("python", "PYTHON")
])
def test_to_uppercase(input_text, expected):
    assert to_uppercase(input_text) == expected


@pytest.mark.parametrize("input_text, expected", [
    ("hello", "olleh"),
    ("abc", "cba"),
    ("123", "321")
])
def test_reverse_string(input_text, expected):
    assert reverse_string(input_text) == expected
    

def test_to_upperscase_with_fixture(sample_text):
    assert to_uppercase(sample_text) == "HELLO"