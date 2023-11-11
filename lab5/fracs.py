def add_frac(frac1, frac2):
  try:
    if frac1[1] == 0 or frac2[0] == 0:
      raise ValueError
    new_denominator = frac1[1] * frac2[1]
    return [(new_denominator/frac1[1]) * frac1[0] + (new_denominator/frac2[1]) * frac2[0], new_denominator]
  except ValueError:
    raise ValueError("Invalid input")

def sub_frac(frac1, frac2):
  try:
    if frac1[1] == 0 or frac2[0] == 0:
      raise ValueError
    new_denominator = frac1[1] * frac2[1]
    return [(new_denominator/frac1[1]) * frac1[0] - (new_denominator/frac2[1]) * frac2[0], new_denominator]
  except ValueError:
    raise ValueError("Invalid input")
def mul_frac(frac1, frac2):
  try:
    if frac1[1] == 0 or frac2[0] == 0:
      raise ValueError
    return [frac1[0] * frac2[0], frac1[1] * frac2[1]]
  except ValueError:
    raise ValueError("Invalid input")

def div_frac(frac1, frac2):
  try:
    if frac1[1] == 0 or frac2[0] == 0:
      raise ValueError
    return [frac1[0] * frac2[1], frac1[1] * frac2[0]]
  except ValueError:
    raise ValueError("Invalid input")

def is_positive(frac):
  try:
    if frac[1] == 0:
      raise ValueError
    if frac[0] == 0:
      return "The number is zero"
    else:
      return frac[0] >= 0 and frac[1] > 0
  except ValueError:
    raise ValueError("Invalid input")

def is_zero(frac):
  try:
    if frac[1] == 0:
      raise ValueError
    return frac[0] == 0
  except ValueError:
    raise ValueError("Invalid input")

def frac2float(frac):
  try:
    if frac[1] == 0:
      raise ValueError
    return frac[0] / frac[1]
  except ValueError:
    raise ValueError("Invalid input")