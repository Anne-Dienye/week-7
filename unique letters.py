#coding
def unique_letters(s):
    return sorted(set(char.lower() for char in s if char.isalpha()))

# Test the function
word = input("Enter a word: ")
result = unique_letters(word)
print(f"Unique letters in '{word}': {result}")