from functools import total_ordering

@total_ordering
class Min(object):
  def __lt__(self, other):
    """
    Min < -sys.maxint #=> True
    Min < None #=> True
    Min < '' #=> True
    """
    if other is Min:
      return False
    return True

@total_ordering
class Max(object):
  """
  Max > Min #=> True
  Max > sys.maxint #=> True
  Max > 99999999999999999 #=> True
  """
  def __gt__(self, other):
    if other is Max:
      return False
    return True

Min = Min()
Max = Max()