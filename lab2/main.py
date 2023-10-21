from line import *
from lista import *


def main():
    line = input("Enter text: ")
    word = input("Enter word: ")
    lista = [2, 105, 320, 52, 6, 70, 90]

    print(f"Number of words: {count_words(line)}")
    print(f"Underscored word: {underscore(word)}")
    print(f"Word created from the first letters: {first_letter_word(line)}")
    print(f"Word created from the last letters: {last_letter_word(line)}")
    print(f"Total lenght of words: {len_of_words(line)}")
    print(f"Longest word: {longest_word(line)} with: {len(longest_word(line))} letters.")
    print(f"Text after finding gvr: {gvr(line)}")
    print(f"Text sorted alphabetically: {alpha_sort(line)}")
    print(f"Text sorted by length of words: {len_sort(line)}")

    print(f"String made of list: {create_string(lista)}")
    count_zeros(lista)
    print(f"numbers from the list in a new format:")
    transform(lista)


if __name__ == '__main__':
    main()