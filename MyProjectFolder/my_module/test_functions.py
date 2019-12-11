import pytest

from anxiety_bot import *

def test_should_continue():
    assert should_continue('a') == True
    assert should_continue('b') == False
    assert should_continue('a') and sc('b') == False

def test_same_input():
    assert isinstance(same_input('B'), str)
    assert same_input('C') == 'c'