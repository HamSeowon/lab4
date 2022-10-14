def countVowles(words):
    numVowels = 0
    for letter in words:
        if letter.lower() in "aeiou":
            numVowels += 1
    return numVowels

#test
print(countVowles("AEIOu"))
