import pytest
import validators

def test_success():
  assert validators.between(1, 0, 2)

def test_failure():
  assert not validators.between(2,3,5)