# 2.15
def create_string(lista):
    return ''.join(str(x) for x in lista)


# 2.18
def count_zeros(lista):
    for x in lista:
        print(f"number of zeros in {x}: {str(x).count('0')}")


# 2.19
def transform(lista):
    for x in lista:
        print(str(x).zfill(3))