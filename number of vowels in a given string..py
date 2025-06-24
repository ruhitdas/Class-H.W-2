def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in s if char in vowels)
    print(f'The number of vowels in "{s}" is {count}.')
    return count
count_vowels("Hello World")
