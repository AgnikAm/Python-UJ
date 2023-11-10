# 4.2
def make_ruler(n):
    ruler = "|...." * n + "|\n"
    for i in range(n + 1):
        if i>= 99:
            ruler += str(i)
            ruler += " " * 2
        elif i>= 9:
            ruler += str(i)
            ruler += " " * 3
        else:
            ruler += str(i)
            ruler += " " * 4

    return ruler

def make_grid(rows, cols):
    grid = ""
    for r in range(rows + 1):
        grid += "+---" * cols + "+\n"
        if r != rows:
            for c in range(cols + 1):
                grid += "|   "
            grid += "\n"

    return grid

# 4.3
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 4.4
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 4.5
def odwracanie(L, left, right):
    while left >= 0 and right < len(L) and left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def rec_odwracanie(L, left, right):
    if left >=0 and right < len(L) and left < right:
        L[left], L[right] = L[right], L[left]
        rec_odwracanie(L, left + 1, right - 1)

# 4.6
def sum_seq(sequence):
    sums = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sums.append(sum(sum_seq(item)))
        else:
            sums.append(item)
    return sums

# 4.7
def flatten(sequence):
    result = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


