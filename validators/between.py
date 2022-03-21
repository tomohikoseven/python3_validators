from .extremes import Max, Min

def between(value, min=None, max=None):
  if min is None and max is None:
    raise AssertionError('At least one of `min` or `max` must be specified.')

  if min is None:
    min = Min
  if max is None:
    max = Max
  return value >= min  and value <= max