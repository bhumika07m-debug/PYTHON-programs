def make_multiplier(n):
  def multiplier(x):
    return x * n
  return multiplier
 times=make_multiplier(3)
 print(times(10))