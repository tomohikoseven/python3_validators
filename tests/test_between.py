import pytest
import validators


@pytest.mark.parametrize(('value', 'min', 'max'),
  [(11, None, None),(11, 13, 12)]
)
def test_raises_assertion_error_for_invalid_args(value, min, max):
  with pytest.raises(AssertionError):
    assert validators.between(value, min=min, max=max)

@pytest.mark.parametrize(('value','min','max'),[
  (12,11,13),
  (12,None,13),
  (12,11,None),
  (12,12,12)
])
def test_returns_true_on_valid_range(value, min, max):
  assert validators.between(value, min=min, max=max)

@pytest.mark.parametrize(('value','min','max'),[
  (12,10,11),
  (12,13,None),
  (12,None,11)
])
def test_returns_false_on_invalid_range(value, min, max):
  assert not validators.between(value, min=min, max=max)