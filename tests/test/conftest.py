import pytest
from app.string_utils import to_uppercase

@pytest.fixture
def sample_text():
    return "hello"

def test_to_upperscase_with_fixture(sample_text):
    assert to_uppercase(sample_text) == "HELLO"