def fibonacci_series(N):
    # Initialize the first two numbers in the series
    fib_series = [0, 1]
    
    # Continue adding numbers to the series until we reach or exceed N
    while True:
        next_fib = fib_series[-1] + fib_series[-2]  # Calculate the next Fibonacci number
        if next_fib > N:  # Stop if the next number is greater than N
            break
        fib_series.append(next_fib)  # Add the next Fibonacci number to the list
    
    return fib_series

# Example usage:
N = int(input("Enter a positive integer N: "))
result = fibonacci_series(N)
print(f"The Fibonacci series up to {N} is: {result}")
