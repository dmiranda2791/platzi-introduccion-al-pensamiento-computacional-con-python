## Raíz cuadrada de un número usando aproximación

objetivo = int(input('Escoge un número: '))
epsilon = 0.0001
paso = epsilon ** 2

print(f'epsilon: {epsilon}, paso: {paso}')
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
  print(abs(respuesta**2 - objetivo), respuesta)
  respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
  print(f'No se encontró la raíz cuadrada de {objetivo}')
else:
  print(f'La raíz cuadrada de {objetivo} es {respuesta}')
