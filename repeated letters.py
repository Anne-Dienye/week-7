#coding
from collections import Counter

# Function to analyze letter frequencies
def frequency_analysis(message):
    # Normalize the message to lowercase and filter alphabetic characters
    filtered_message = [char.lower() for char in message if char.isalpha()]
    
    # Count the frequency of each letter
    letter_counts = Counter(filtered_message)
    
    # Get the six most common letters
    most_common = letter_counts.most_common(6)
    
    # Display the results
    print("Most common letters:")
    for letter, count in most_common:
        print(f"{letter}: {count}")

# Test the function
message = input("Enter a message: ")
frequency_analysis(message)