from app.string_utils import to_uppercase, reverse_string

def test_to_uppercase():
    assert to_uppercase("hello") =="HELLO"
    
def test_reverse_string():
    assert reverse_string("hello") == "olleh"