def fibonacci_series_till_n(N):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    # List to store the Fibonacci series
    fib_series = []

    # Generate Fibonacci numbers until the next number is greater than N
    while a <= N:
        fib_series.append(a)
        # Update the next Fibonacci number
        a, b = b, a + b

    return fib_series

# Example usage:
N = int(input("Enter a positive integer N: "))
result = fibonacci_series_till_n(N)
print(f"The Fibonacci series till {N} is: {result}")
