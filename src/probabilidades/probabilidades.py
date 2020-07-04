import random

def tirar_dado(numero_de_tiros):
  secuencia_de_tiros = []

  for _ in range(numero_de_tiros):
    tiro = random.choice(list(range(1, 7)))
    secuencia_de_tiros.append(tiro)
  
  return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
  tiros = []

  for _ in range(numero_de_intentos):
    secuencia_de_tiros = tirar_dado(numero_de_tiros)
    tiros.append(secuencia_de_tiros)

  tiros_con_1 = 0
  for tiro in tiros:
    if 1 not in tiro:
      tiros_con_1 += 1 

  probabilidad_tiros_con_1 = tiros_con_1/len(tiros)

  print(f'Probabilidad de no obtener por lo menos un 1 en {numero_de_tiros} es igual {probabilidad_tiros_con_1}')
if __name__ == '__main__':
  numero_de_tiros = int(input('Cuántos tiros del dado: '))
  numero_de_intentos = int(input('Cuántos intentos? '))

  main(numero_de_tiros, numero_de_intentos)