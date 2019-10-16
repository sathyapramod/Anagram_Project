Enter_words = input("Enter the letter")
print(type(Enter_words))
sorted_words = sorted(Enter_words)
print(sorted_words)

keywords = []

from itertools import product

# keywords = itertools.product(sorted_words, repeat=3)

keywords = [''.join(i) for i in product(Enter_words, repeat=3)]
print(keywords)

filename = 'dict.txt'

def words(fname):
    words = {}
    with open(fname) as f:
        for line in f:
            word = line.strip()
            words[word] = 1
    return words

word_dict = words(filename)
print(word_dict)
