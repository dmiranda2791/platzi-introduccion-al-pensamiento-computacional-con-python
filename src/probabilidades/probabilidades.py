import random

def tirar_dado(numero_de_tiros):
  secuencia_de_tiros = []

  for _ in range(numero_de_tiros):
    tiro_1 = random.choice(list(range(1, 7)))
    tiro_2 = random.choice(list(range(1, 7)))
    resultado = tiro_1 + tiro_2
    secuencia_de_tiros.append(resultado)
  
  return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
  tiros = []

  for _ in range(numero_de_intentos):
    secuencia_de_tiros = tirar_dado(numero_de_tiros)
    tiros.append(secuencia_de_tiros)

  tiros_con_12 = 0
  for tiro in tiros:
    if 12 in tiro:
      tiros_con_12 += 1 

  probabilidad_tiros_con_1 = tiros_con_12/len(tiros)

  print(f'Probabilidad de  obtener por lo menos un 12 en {numero_de_tiros} es igual {probabilidad_tiros_con_1}')
if __name__ == '__main__':
  numero_de_tiros = int(input('Cuántos tiros del dado: '))
  numero_de_intentos = int(input('Cuántos intentos? '))

  main(numero_de_tiros, numero_de_intentos)