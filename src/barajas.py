import random
import collections
PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

def crear_baraja():
  barajas = []
  for palo in PALOS:
    for valor in VALORES:
      barajas.append((palo, valor))

  return barajas

def obtener_mano(barajas, tamano_mano):
  mano = random.sample(barajas, tamano_mano)

  return mano

def main(tamano_mano, intentos):
  barajas = crear_baraja()
  
  manos = []
  for _ in range(intentos):
    mano = obtener_mano(barajas, tamano_mano)
    manos.append(mano)

  corrida = 0
  for mano in manos:
    palos = []
    for carta in mano:
      palos.append(carta[0])
  
    counter = dict(collections.Counter(palos))

    for val in counter.values():
      if (val == 5):
        corrida += 1
        break
  
  probabilidad_par = corrida / intentos


  print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')


def probabilidad_escalera_real(tamano_mano, intentos):
  barajas = crear_baraja()

  manos = []
  for _ in range(intentos):
    mano = obtener_mano(barajas, tamano_mano)
    manos.append(mano)

  escalera_real = 0

  for mano in manos:
    counter = {}
    for carta in mano:

      (palo, valor) = carta
      if (valor in ['10', 'jota', 'reina', 'rey']):
        if (palo not in counter):
          counter[palo] = [valor]
        else:
          cartas = counter.get(palo)
          cartas.append(valor)

    for count in counter.values():
      if (len(count) == 4):
        escalera_real += 1
  
  probabilidad_escalera_real = escalera_real / intentos
  print(f'La probabilidad de obtener una escalera real en una mano de {tamano_mano} barajas es {probabilidad_escalera_real}')


  

if __name__ == '__main__':
  tamano_mano = int(input('Tamano de mano?: '))
  intentos = int(input('Intentos para calcular la probabilidad?: '))

  # main(tamano_mano, intentos)
  probabilidad_escalera_real(tamano_mano, intentos)
