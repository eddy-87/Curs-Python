def is_palindrome(text):
    s = "".join(text.lower().split())
    return s == s[::-1]

text = "A man a plan a canal Panama"
print(is_palindrome(text))
