from .extremes import Max, Min

def between(value, min=None, max=None):
  if min is None and max is None:
    raise AssertionError('At least one of `min` or `max` must be specified.')

  if min is None:
    min = Min
  if max is None:
    max = Max

  try:
    min_gt_max = min > max
  except TypeError:
    min_gt_max = max < min
  if min_gt_max:
    raise AssertionError('`min` cannot be more than `max`.')


  return min <= value  and value <= max