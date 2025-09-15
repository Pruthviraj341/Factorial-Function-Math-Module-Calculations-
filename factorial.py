# Factorial using loop
def factorial(n):
    if n < 0:
        return None   # factorial not defined for negative integers
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Main program
while True:
    try:
        num = int(input("Enter an integer (type 0 to exit): "))

        if num == 0:
            print("Exiting program. Goodbye!")
            break

        fact = factorial(num)
        if fact is None:
            print(f"Factorial is not defined for negative integer {num}.")
        else:
            print(f"Factorial of {num} is: {fact}")

    except ValueError:
        print("Invalid input! Please enter an integer.")
