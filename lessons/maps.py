from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)

words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

# normal method
# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)


# maps methods
print(list(map(jumble, words)))


# list comprehension method
print( [ jumble(word) for word in words ] )
