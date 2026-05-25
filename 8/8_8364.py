from itertools import *

word = sorted("ЛИНКОР")

letters = [''.join(x) for x in product(word, repeat=4)]
print(letters.index('КИНО') + 1)
