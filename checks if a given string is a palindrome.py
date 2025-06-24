def is_palindrome(s):
    s = s.replace(" ", "").lower()
    if s == s[::-1]:
        print(f'"{s}" is a palindrome.')
        return True
    else:
        print(f'"{s}" is not a palindrome.')
        return False
is_palindrome("Racecar")
is_palindrome("Hello")
