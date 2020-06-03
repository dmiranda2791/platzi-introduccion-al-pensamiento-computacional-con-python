usuario_1 = input('Cuál es el nombre de la persona 1: ')
edad_usuario_1 = int(input('Cuál es la edad de la persona 1: '))
usuario_2 = input('Cuál es el nombre de la persona 2:')
edad_usuario_2 = int(input('Cuál es la edad de la persona 2: '))

if (edad_usuario_1 > edad_usuario_2):
  print(f'{usuario_1} ({edad_usuario_1}) es mayor que {usuario_2} ({edad_usuario_2})')
elif (edad_usuario_2 > edad_usuario_1):
  print(f'{usuario_2} ({edad_usuario_2}) es mayor que {usuario_1} ({edad_usuario_1})')
else:
  print(f'{usuario_1} ({edad_usuario_1}) y {usuario_2}({edad_usuario_2}) tienen la misma edad')