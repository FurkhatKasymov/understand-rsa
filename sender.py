from transformer import word_to_number
from raise_with_modulo import raise_with_modulo

print('Enter public key')
e = int(input('e:'))
n = int(input('n:'))

original = n + 1
while original > n:
    original_msg = input('Enter message to encrypt:')
    original = word_to_number(original_msg)
    
encrypted = raise_with_modulo(original, e, n)
print(encrypted)
