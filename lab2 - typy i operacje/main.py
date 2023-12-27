from string_operations import *
from nums_operations import *

def get_numbers():
    numbers = []
    while True:
        try:
            user_input = input("Enter a number (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
    return numbers

def main():
    line = input("Enter text: ")
    word = input("Enter word: ")
    L = get_numbers()

    print(f"Number of words: {count_words(line)}")
    print(f"Underscored word: {underscore(word)}")
    print(f"Word created from the first letters: {first_letter_word(line)}")
    print(f"Word created from the last letters: {last_letter_word(line)}")
    print(f"Total lenght of words: {len_of_words(line)}")
    print(f"Longest word: {longest_word(line)} with: {len(longest_word(line))} letters.")
    print(f"Text after finding gvr: {gvr(line)}")
    print(f"Text sorted alphabetically: {alpha_sort(line)}")
    print(f"Text sorted by length of words: {len_sort(line)}")

    print(f"String made of list: {create_string(L)}")
    for x in L:
        print(f"zeros in {x}: {count_zeros(x)}")
    print(f"numbers from the list in a new format:")
    for x in L:
        print(transform(x))

if __name__ == '__main__':
    main()