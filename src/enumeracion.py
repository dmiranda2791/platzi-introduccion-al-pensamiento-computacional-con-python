# Determinar si el número tiene raíz exacta

objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo:
  respuesta += 1

if (respuesta**2 == objetivo):
  print(f'La raíz cuadrada de objetivo es: {respuesta}')
else:
  print(f'El objetivo no tiene raíz cuadrada exacta')