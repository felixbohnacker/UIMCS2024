def fibonacci_series_upto_n(N):
    # Initializing the first two Fibonacci numbers
    fib_series = [0, 1]
    
    # Generating Fibonacci numbers until the next number exceeds N
    while True:
        next_fib = fib_series[-1] + fib_series[-2]
        if next_fib > N:
            break
        fib_series.append(next_fib)
    
    # If N is part of the Fibonacci series, include it
    return fib_series

# Test the function with an example
N = 21
result = fibonacci_series_upto_n(N)
print(f"Fibonacci series up to {N}: {result}")
