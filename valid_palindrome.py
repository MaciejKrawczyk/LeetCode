
s = "A man, a plan, a canal: Panama"


def palindrome(s):
    s = ''.join(c for c in s.lower() if c.isalnum())
    return s == s[::-1]

print(palindrome(s))