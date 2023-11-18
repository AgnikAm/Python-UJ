from math import gcd

def check_denominator(frac):
  if frac[1] == 0:
    raise ZeroDivisionError("Invalid input: zero in the denominator")

def add_frac(frac1, frac2):
  check_denominator(frac1)
  check_denominator(frac2)

  new_denominator = frac1[1] * frac2[1]

  return [(new_denominator / frac1[1]) * frac1[0] + (new_denominator / frac2[1]) * frac2[0], new_denominator]

def sub_frac(frac1, frac2):
  check_denominator(frac1)
  check_denominator(frac2)

  new_denominator = frac1[1] * frac2[1]
  new_numerator = (new_denominator/frac1[1]) * frac1[0] - (new_denominator/frac2[1]) * frac2[0]

  return [new_numerator, new_denominator]

def mul_frac(frac1, frac2):
  check_denominator(frac1)
  check_denominator(frac2)

  return [frac1[0] * frac2[0], frac1[1] * frac2[1]]

def div_frac(frac1, frac2):
  check_denominator(frac1)
  check_denominator(frac2)

  if frac2[0] == 0:
    raise ValueError

  return [frac1[0] * frac2[1], frac1[1] * frac2[0]]


def is_positive(frac):
  check_denominator(frac)

  if frac[0] == 0:
    return "The number is zero"
  else:
    return (frac[0] >= 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0)


def is_zero(frac):
  check_denominator(frac)

  return frac[0] == 0


def simplify(frac):
  simplified_frac = [frac[0] / gcd(frac[0], frac[1]), frac[1] / gcd(frac[0], frac[1])]
  return simplified_frac


def sign_compatibility(frac1, frac2):
  return (is_positive(frac1) == is_positive(frac2))


def cmp_frac(frac1, frac2):
  check_denominator(frac1)
  check_denominator(frac2)

  simplified_frac1 = simplify(frac1)
  simplified_frac2 = simplify(frac2)

  if (sign_compatibility(simplified_frac1, simplified_frac2)):
    simplified_frac1 = [x if x >= 0 else -x for x in simplified_frac1]
    simplified_frac2 = [x if x >= 0 else -x for x in simplified_frac2]
  elif is_positive(frac1):
    return 1
  else: return -1

  if simplified_frac1 < simplified_frac2:
    return -1
  elif simplified_frac1 > simplified_frac2:
    return 1
  else: return 0


def frac2float(frac):
  check_denominator(frac)

  return frac[0] / frac[1]