

def aproximacion():
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


def busqueda_binaria():
  objetivo = int(input('Escoge un número: '))
  epsilon = 0.01
  bajo = 0.0
  alto = max(1.0, objetivo)
  respuesta = (alto + bajo)/2

  while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo=0{bajo}, alto={alto}, respuesta={respuesta}')
    if(respuesta**2 < objetivo):
      bajo = respuesta
    else:
      alto = respuesta

    respuesta = (alto + bajo)/2

  print(f'La raíz cuadrada de {objetivo} es {respuesta}')

def enumeracion():
  objetivo = int(input('Escoge un entero: '))
  respuesta = 0

  while respuesta**2 < objetivo:
    respuesta += 1

  if (respuesta**2 == objetivo):
    print(f'La raíz cuadrada de objetivo es: {respuesta}')
  else:
    print(f'El objetivo no tiene raíz cuadrada exacta')

def print_menu():
  print('Escoge un algoritmo: ')
  print('1) Enumeración')
  print('2) Aproximación')
  print('3) Búsqueda Binaria')

print_menu()
algoritmo = int(input(''))

if (algoritmo == 1):
  enumeracion()
elif (algoritmo == 2):
  aproximacion()
elif (algoritmo == 3):
  busqueda_binaria()
else:
  print(f'{algoritmo} no es una opción valida')