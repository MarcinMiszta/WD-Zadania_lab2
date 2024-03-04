import sys

text = input('Enter a word: ')
text2 = []
text3 = ""
text2.extend(text)
text2.reverse()
for char in text2:
    text3 += char
if text3 == text:
    print('The word is a palindrome')
else:
    print('The word is NOT a palindrome')

