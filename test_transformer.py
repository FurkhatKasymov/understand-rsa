from transformer import word_to_number, number_to_word


assert word_to_number('a')   == 1
assert word_to_number('abc') == 2081, "1 + 2*26 + 3*26^2"
assert word_to_number('hello') == 7073802, "8 + 5*26 + 12*26^2 + 12*26^3 + 15*26^4"


assert number_to_word(1) == 'a'
assert number_to_word(2081) == 'abc'
assert number_to_word(7073802) == 'hello'
