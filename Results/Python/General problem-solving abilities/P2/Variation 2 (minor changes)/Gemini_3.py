def fibonacci_series(n):
  """Calculates the Fibonacci series up to the given number.

  Args:
    n: The maximum number in the series.

  Returns:
    A list containing the Fibonacci series up to n.
  """

  if n <= 0:
    return []

  fib_series = [0, 1]
  while fib_series[-1] < n:
    next_fib = fib_series[-1] + fib_series[-2]
    fib_series.append(next_fib)

  # If n is in the series, keep it
  if fib_series[-1] == n:
    return fib_series
  else:
    return fib_series[:-1]

# Example usage:
n = 20
result = fibonacci_series(n)
print(result)