def factorial(n):
  """Calcula el factorial de n

  n int > 0
  returns n!
  """

  if (n == 1):
    return 1
  else:
    return n * factorial(n - 1)

n = int(input('Escoge un número: '))
resultado = factorial(n)
print(f'El factorial de n es {resultado}')