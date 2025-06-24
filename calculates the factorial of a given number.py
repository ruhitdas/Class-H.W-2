def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"The factorial of {n} is {result}")
    return result
factorial(5)
