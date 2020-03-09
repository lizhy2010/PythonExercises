# Palindrome Exercise

string = input("Enter a word: ")

if string.lower() == string[::-1].lower():
    print("'%s' is a palindrome!" % string)
else:
    print("'%s' is not a palindrome." % string)
