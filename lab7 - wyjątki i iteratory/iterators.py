import itertools
import random

iter_zero_one = itertools.cycle([0, 1])
iter_NESW = (random.choice(["N", "E", "S", "W"]) for _ in iter(int, 1))
iter_day = itertools.cycle([0, 1, 2, 3, 4, 5, 6])

for _ in range(5):
    print(next(iter_zero_one))

for _ in range(5):
    print(next(iter_NESW))

for _ in range(14):
    print(next(iter_day))
