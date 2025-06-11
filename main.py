
def factorial(num: int) -> int:
    count = 1
    for i in range(2, num + 1):
        count *= i
    return count

num = 4
print(f"Factorial of ({num}) = {factorial(num)}")