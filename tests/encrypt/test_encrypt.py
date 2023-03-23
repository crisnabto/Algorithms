from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("awesome algorithms!", 0) == "!smhtirogla emosewa"

    assert encrypt_message("awesome algorithms!", 5) == "osewa_!smhtirogla em"

    with pytest.raises(TypeError):
        encrypt_message("awesome algorithms!", "not a number")
