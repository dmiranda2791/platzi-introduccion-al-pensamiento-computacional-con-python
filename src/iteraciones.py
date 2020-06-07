contador_interno = 0
contador_externo = 0

while contador_externo < 5:
  while contador_interno < 6:
    print(contador_externo, contador_interno)
    contador_interno += 1

    if (contador_interno >= 3):
      break
  contador_externo += 1
  contador_interno = 0


paises = {
  'Honduras': 'Tegucigalpa',
  'Costa Risa': 'San José',
  'Nicaragua': 'Managua',
  'El Salvador': 'San Salvador',
  'Guatemala': 'Guatemala',
  'Pánama': 'Panama',
}

print('\n')
for key in paises:
  print(f'La capital de {key} es {paises[key]}')

print('\n')
for key in paises.keys():
  print(f'La capital de {key} es {paises[key]}')

print('\n')
for value in paises.values():
  print(f'La capital de ... es {value}')

print('\n')
for item in paises.items():
  (pais, capital) = item
  print(f'La capital de {pais} es {capital}')

'Paraguay' in paises

# Dict comprehensions
{key: value for (key, value) in paises.items()}