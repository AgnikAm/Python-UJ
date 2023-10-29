def not_divisible_by_3():
    for i in range(31):
        if i%3:
            print(i)

def third_pow():
    while(True):
        x = input("Please enter the number that will be raised to the third power or enter stop to interrupt the operation: ")
        if x.lower() == 'stop':
            break
        elif x.isnumeric():
            print(f"{x}^3 is {int(x)**3}")
        else:
            print("Wrong input. Please enter a number or 'stop'")

def ruler(length):
    print("|...." * length, end = "")
    print("|")
    for i in range(length + 1):
        if i>= 99:
          print(i, " ", end = "")
        elif i>= 9:
          print(i, " " * 2, end = "")
        else:
          print(i, " " * 3, end = "")

def rectangle(rows, cols):
    for r in range(rows+1):
        print("+---" * cols, end="")
        print("+\n")
        if r != rows:
          for c in range(cols+1):
            print("|", "  ", end="")
          print("\n")

def duplicated_elements(a, b):
    duplicates = []
    for elem_a in a:
        if elem_a in b and elem_a not in duplicates:
          duplicates.append(elem_a)

    return duplicates

def common_elements(a, b):
    elements = []
    for elem_a in a:
        if elem_a not in elements:
          elements.append(elem_a)
    for elem_b in b:
        if elem_b not in elements:
          elements.append(elem_b)

    return elements

def sum_sequence(a):
    sum_array = []
    for elem in a:
        sum = 0
        for digit in elem:
          sum += digit
        sum_array.append(sum)

    return sum_array