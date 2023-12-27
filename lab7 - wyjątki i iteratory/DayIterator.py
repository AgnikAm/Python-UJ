class DayIterator:
    def __init__(self):
        self.current_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current_value
        self.current_value = (self.current_value + 1) % 7
        return result