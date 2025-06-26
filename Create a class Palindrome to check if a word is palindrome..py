


class Palindrome:
    text=input("enter text")
    def plain(text):
        if text==text[::-1]:
            print("true")
        else:
            print("false")
    plain(text)
