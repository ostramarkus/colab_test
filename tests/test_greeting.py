import pytest
import main

def test_greeting():
    assert(main.create_greeting() == "Hello!")