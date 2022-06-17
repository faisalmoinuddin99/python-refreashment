# Create a dictionary and take input from the user and return the meaning of the word from the dictionary

oxfordDictionary =  {
    "mutuable":"Can be change",
    "immutuable":"Cannot change",
    "buzzkill":"Person or thing that has a depressing effect",
    "chillax":"To calm down and relax"
}

searchWord = input("Enter a word:")
normalizedWords = searchWord.lower()
print(oxfordDictionary[normalizedWords])

# output
"""
Enter a word:buzzkill 
Person or thing that has a depressing effect
"""