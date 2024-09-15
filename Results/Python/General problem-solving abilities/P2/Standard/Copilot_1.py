def fibonacci_series(N):
    # Initialize the first two Fibonacci numbers
    fib_series = [0,1]
    # Generate the Fibonacci series until the next number exceeds N
    while True: 
        next_fib = fib_series[-1] + fib_series[-2]
        if next_fib > N: 
            break
        fib_series.append(next_fib)
    
    # Include N if it is part of the series
    if N not in fib_series: 
        fib_series.append(N)
    return fib_series
# Example usage
N = 21
print(fibonacci_series(N))