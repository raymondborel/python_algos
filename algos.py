
'''
******************************************************************************
Write a function reverse_string(string) that takes in a hyphenated string and
returns a the hyphenated string reversed.

Examples:
reverse_string('Go-to-the-store') #=> 'store-the-to-Go'
reverse_string('Jump-jump-for-joy') #=> 'joy-for-jump-Jump,'
******************************************************************************
'''

def reverse_hyphenated_string(string):
    words = string.split('-')  # Split the string into a list of words
    reversed_words = reversed(words)  # Reverse the order of the words
    reversed_string = '-'.join(reversed_words)  # Join the reversed words with hyphens
    return reversed_string

