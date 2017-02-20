import math
from generate_prime import generate_prime
from relative_prime import relative_prime
from transformer import number_to_word
from pulverizer import pulverizer
from raise_with_modulo import raise_with_modulo


p = generate_prime()
q = generate_prime()
n = p*q
fi = (p - 1) * (q - 1)
e = relative_prime(fi)
d, _ = pulverizer(e, fi)
d = (d + math.ceil((-1*d)/fi) * fi) if d < 0 else d
print('Your public key is')
print('e:', e)
print('n:', n)

encrypted = int(input('Enter encrypted message:'))
decrypted = raise_with_modulo(encrypted, d, n)

print('The message is:', number_to_word(decrypted))
