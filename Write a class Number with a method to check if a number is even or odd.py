class number:
    number=int(input("enter the number"))
    def check_even_odd(number):
        if number % 2 == 0:
            print("even")
        else:
            print("odd")
    check_even_odd(number)