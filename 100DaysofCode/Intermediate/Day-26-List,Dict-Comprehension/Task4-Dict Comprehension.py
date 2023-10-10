"""
Instructions
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.
"""
sentence = input()
# 🚨 Don't change code above 👆
# Write your code below 👇

result = {
    word: len(word) for word in sentence.split(' ')
}

print(result)
