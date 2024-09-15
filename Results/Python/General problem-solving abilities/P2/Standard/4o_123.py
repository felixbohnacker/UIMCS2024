1:

def fibonacci_series_upto_n(N):
    # Initializing the first two Fibonacci numbers
    fib_series = [0, 1]
    
    # Continue generating Fibonacci numbers until the last number is greater than or equal to N
    while True:
        next_fib = fib_series[-1] + fib_series[-2]
        if next_fib > N:
            break
        fib_series.append(next_fib)
    
    # If N is not 0 or 1, filter the series to exclude 0 if N > 0, or return [0] if N is 0
    if N == 0:
        return [0]
    elif N == 1:
        return [0, 1]
    else:
        return [num for num in fib_series if num <= N]

# Example usage:
N = 21
result = fibonacci_series_upto_n(N)
print("Fibonacci series up to", N, ":", result)


2:

def fibonacci_series_upto_n(N):
    # Initializing the first two Fibonacci numbers
    fib_series = [0, 1]
    
    # Generate Fibonacci numbers until the next number exceeds N
    while True:
        next_fib = fib_series[-1] + fib_series[-2]
        if next_fib > N:
            break
        fib_series.append(next_fib)
    
    # Handle the case when N is less than 1
    if N == 0:
        return [0]
    
    # Filter the series to only include numbers up to N
    return [num for num in fib_series if num <= N]

# Example usage:
N = 21
result = fibonacci_series_upto_n(N)
print(result)


3:

def fibonacci_series_till_n(N):
    # Initialize the first two Fibonacci numbers
    fib_series = [0, 1]
    
    # Generate the Fibonacci series until the next number would exceed N
    while True:
        next_fib = fib_series[-1] + fib_series[-2]
        if next_fib > N:
            break
        fib_series.append(next_fib)
    
    # Check if N is not in the series and remove the initial 0 if N is less than 1
    if N < 1:
        fib_series = fib_series[1:]
    
    return fib_series

# Example usage:
N = 21
result = fibonacci_series_till_n(N)
print("Fibonacci series up to", N, ":", result)

