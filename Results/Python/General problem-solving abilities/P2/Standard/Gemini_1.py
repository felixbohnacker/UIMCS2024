def fibonacci_series(N):
  """Calculates the Fibonacci series up to N.

  Args:
    N: A positive integer.

  Returns:
    A list containing the Fibonacci series up to N.
  """

  fib_series = [0, 1]
  while fib_series[-1] <= N:
    next_fib = fib_series[-1] + fib_series[-2]
    fib_series.append(next_fib)

  return fib_series

# Example usage:
N = 20
result = fibonacci_series(N)
print(result)