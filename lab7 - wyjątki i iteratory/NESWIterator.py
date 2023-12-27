import random
class NESWIterator:
    def __init__(self):
        self.current_value = random.choice(["N", "E", "S", "W"])

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current_value
        self.current_value = random.choice(["N", "E", "S", "W"])
        return result