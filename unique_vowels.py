vowels = ['a', 'e', 'i', 'o', 'u']
word = input("provide a word to search in: ")
uniquevowels = []
for letter in word:
    if letter in vowels:
        if letter not in uniquevowels:
            uniquevowels.append(letter)
for vowel in uniquevowels:
    print(vowel)