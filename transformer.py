import string


alphabet = string.ascii_lowercase
number_of_letters = len(alphabet)

def word_to_number(word):
    code = 0
    for i in range(len(word)):
        letter_code = alphabet.index(word[i]) + 1
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


def test():
    assert word_to_number('a')   == 1
    assert word_to_number('abc') == 2081, "1 + 2*26 + 3*26^2"
    assert word_to_number('hello') == 7073802, "8 + 5*26 + 12*26^2 + 12*26^3 + 15*26^4"
    
    assert number_to_word(1) == 'a'
    assert number_to_word(2081) == 'abc'
    assert number_to_word(7943967612) == 'victory'

if __name__ == '__main__':
    test()
    print('test pass')
