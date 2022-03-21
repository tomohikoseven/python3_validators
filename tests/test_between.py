import pytest
import validators

def test_success():
  assert validators.between(1, 0, 2)

def test_failure():
  assert not validators.between(2,3,5)

@pytest.mark.parametrize(('value', 'min', 'max'), [(12, None, None)])
def test_raises_assertion_error_for_invalid_args(value, min, max):
  with pytest.raises(AssertionError):
    assert validators.between(value, min=min, max=max)

@pytest.mark.parametrize(('value','min','max'),[
  (12,None,13),
])
def test_returns_true_on_valid_range(value, min, max):
  assert validators.between(value, min=min, max=max)