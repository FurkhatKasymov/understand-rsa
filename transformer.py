import string


alphabet = string.ascii_lowercase
number_of_letters = 26


def word_to_number(word):
    code = 0
    for i in range(len(word)):
        letter_code = string.ascii_lowercase.index(word[i]) + 1
        code += letter_code * (number_of_letters ** i)
    return code


def number_to_word(number):
    letters = []
    while number != 0:
        position = number % number_of_letters
        letter = alphabet[position - 1]
        letters.append(letter)
        number //= number_of_letters
    return ''.join(letters)
