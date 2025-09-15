import math

# Ask user for input
try:
    num = float(input("Enter a number: "))

    # Square root
    if num < 0:
        sqrt_val = "Square root not defined for negative numbers."
    else:
        sqrt_val = math.sqrt(num)

    # Natural logarithm
    if num <= 0:
        log_val = "Logarithm not defined for zero or negative numbers."
    else:
        log_val = math.log(num)

    # Sine (in radians)
    sine_val = math.sin(num)

    # Display results
    print("\n--- Results ---")
    print(f"Square root of {num} = {sqrt_val}")
    print(f"Natural log of {num} = {log_val}")
    print(f"Sine of {num} (radians) = {sine_val}")

except ValueError:
    print("Invalid input! Please enter a valid number.")
