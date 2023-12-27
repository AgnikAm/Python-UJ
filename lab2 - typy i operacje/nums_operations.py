# 2.15
def create_string(L):
    return ''.join(str(x) for x in L)

# 2.18
def count_zeros(num):
    return str(num).count('0')

# 2.19
def transform(num):
    return str(num).zfill(3)