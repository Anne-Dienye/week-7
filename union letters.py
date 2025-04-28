#coding
def union_letters(word1, word2):
    return sorted(set(word1.lower()).union(set(word2.lower())))

# Function to get letters in both words (Intersection)
def intersection_letters(word1, word2):
    return sorted(set(word1.lower()).intersection(set(word2.lower())))

# Function to get letters in either word but not both (Symmetric Difference)
def symmetric_difference_letters(word1, word2):
    return sorted(set(word1.lower()).symmetric_difference(set(word2.lower())))

# Test the functions
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

print(f"Letters in at least one word: {union_letters(word1, word2)}")
print(f"Letters in both words: {intersection_letters(word1, word2)}")
print(f"Letters in either word but not both: {symmetric_difference_letters(word1, word2)}")