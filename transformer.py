import string


alphabet = string.ascii_lowercase
base = len(alphabet) + 1

def word_to_number(word):
    code = 0
    for i in range(len(word)):
        letter_code = alphabet.index(word[i]) + 1
        code += letter_code * (base ** i)
    return code

def number_to_word(number):
    letters = []
    while number != 0:
        position = number % base
        letter = alphabet[position - 1]
        letters.append(letter)
        number //= base
    return ''.join(letters)


def test():
    assert word_to_number('a')       == 1
    assert word_to_number('abc')     == 2242, "1 + 2*27 + 3*27^2"
    assert word_to_number('victory') == 9952160278
    assert word_to_number('zd')      == 134
    
    assert number_to_word(1)          == 'a'
    assert number_to_word(2242)       == 'abc'
    assert number_to_word(9952160278) == 'victory'
    assert number_to_word(134)        == 'zd'

if __name__ == '__main__':
    test()
    print('test pass')
