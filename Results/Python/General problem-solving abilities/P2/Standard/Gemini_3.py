def fibonacci_series(n):
  """Calculates the Fibonacci series up to the given number N.

  Args:
    n: A positive integer.

  Returns:
    A list containing the Fibonacci series up to N.
  """

  fib_series = [0, 1]
  while fib_series[-1] <= n:
    fib_series.append(fib_series[-1] + fib_series[-2])
  return fib_series[:len(fib_series) - 1]

# Example usage:
n = 100
result = fibonacci_series(n)
print(result)