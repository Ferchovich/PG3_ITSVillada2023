import pytest
import re

def validate_password(password: str):
    if len(password) < 8:
        return False
    
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password) or not re.search(r"\d", password):
        return False
    
    if re.search(r"[^A-Za-z0-9]", password):
        return False
    return True



@pytest.mark.parametrize("password, expected_result", [
    ("Abcdefg1", True),
    ("Abcdefg1#", False),
    ("abcdefgh", False),
    ("ABCDEFG1", False),
    ("12345678", False),
])

def test_validate_password(password, expected_result):
    assert validate_password(password) == expected_result
