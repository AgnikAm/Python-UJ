# 2.10
def count_words(text):
    return len(text.split())

# 2.11
def underscore(word):
    return "_".join(word)

# 2.12
def first_letter_word(text):
    return ''.join(word[0] for word in text.split())

def last_letter_word(text):
    return ''.join(word[-1] for word in text.split())

# 2.13
def len_of_words(text):
    return (sum(len(word) for word in text.split()))

# 2.14 a) b)
def longest_word(text):
    return max(text.split(), key = len)

# 2.16
def gvr(text):
    text = text.replace("GvR", "Guido van Rossum")
    return text

# 2.17
def alpha_sort(text):
    return sorted(text.split(), key = str.casefold)

def len_sort(text):
    return sorted(text.split(), key = len)