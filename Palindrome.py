def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("Palindrome")
else:
    print("Not a palindrome")
