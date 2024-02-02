def fl_pt_sys(base, k, m, M, number, chop=True):
  """Returns a number in a given floating point system"""
  number_base = number_to_base(number, base)
  num_split = num_split(number_base)
  exp = exponent(number, m, M)
  
  if chop == True:
    num_split = float(num_split[:k].join(''))
  else:
    num_split = round(float(num_split[:k+1].join('')), k)
    
  num_real =  num_split * base ** exp
  return number_real

def num_split(number):
  """Returns a tuple of the digits of a number"""
  number_str = str(number)
  tuple = []
  for i in range(len(number)):
    tuple = tuple.append(number[i])
  return tuple

def number_to_base(n, b):
  """Returns a number in a given base b"""
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def exponent(number, m, M):
  """Returns the exponent of a number with in a certain bound""""
  exp = len(number)
  if exp > M:
    exp = M
  elif exp < m:
    exp = m
  return exp
    
