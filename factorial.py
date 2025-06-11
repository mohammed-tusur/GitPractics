
def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    count = 1
    for i in range(2, num + 1):
        count *= i
    return count
