from math import gcd
import numpy as np

def check_denominator(frac):
  if frac[1] == 0:
    raise ValueError("Invalid input: zero in the denominator")

def add_frac(frac1, frac2):
  try:
    check_denominator(frac1)
    check_denominator(frac2)

    new_denominator = frac1[1] * frac2[1]
    return [(new_denominator/frac1[1]) * frac1[0] + (new_denominator/frac2[1]) * frac2[0], new_denominator]

  except ValueError:
    raise ValueError

def sub_frac(frac1, frac2):
  try:
    check_denominator(frac1)
    check_denominator(frac2)

    new_denominator = frac1[1] * frac2[1]
    return [(new_denominator/frac1[1]) * frac1[0] - (new_denominator/frac2[1]) * frac2[0], new_denominator]

  except ValueError:
    raise ValueError

def mul_frac(frac1, frac2):
  try:
    check_denominator(frac1)
    check_denominator(frac2)

    return [frac1[0] * frac2[0], frac1[1] * frac2[1]]

  except ValueError:
    raise ValueError

def div_frac(frac1, frac2):
  try:
    check_denominator(frac1)
    check_denominator(frac2)

    if frac2[0] == 0:
      raise ValueError

    return [frac1[0] * frac2[1], frac1[1] * frac2[0]]

  except ValueError:
    raise ValueError

def is_positive(frac):
  try:
    check_denominator(frac)

    if frac[0] == 0:
      return "The number is zero"
    else:
      return frac[0] >= 0 and frac[1] > 0

  except ValueError:
    raise ValueError

def is_zero(frac):
  try:
    check_denominator(frac)

    return frac[0] == 0

  except ValueError:
    raise ValueError

def simplify(frac):
  simplified_frac = [frac[0] / gcd(frac[0], frac[1]), frac[1] / gcd(frac[0], frac[1])]
  return simplified_frac

def sign_compatibility(frac1, frac2):
  return np.sum(np.array(frac1) < 0, axis=0) == np.sum(np.array(frac2) < 0, axis=0)

def cmp_frac(frac1, frac2):
  try:
    check_denominator(frac1)
    check_denominator(frac2)

    simplified_frac1 = simplify(frac1)
    simplified_frac2 = simplify(frac2)

    if(sign_compatibility(simplified_frac1, simplified_frac2)):
      simplified_frac1 = [x if x >= 0 else -x for x in simplified_frac1]
      simplified_frac2 = [x if x >= 0 else -x for x in simplified_frac2]

    if simplified_frac1 < simplified_frac2:
      return -1
    elif simplified_frac1 > simplified_frac2:
      return 1
    else: return 0

  except ValueError:
    raise ValueError

def frac2float(frac):
  try:
    check_denominator(frac)

    return frac[0] / frac[1]

  except ValueError:
    raise ValueError