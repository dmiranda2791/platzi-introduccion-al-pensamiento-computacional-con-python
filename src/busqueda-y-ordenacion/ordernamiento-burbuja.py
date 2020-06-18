import random

def ordenamiento_burbuja(lista):
  n = len(lista)
  for i in range(n):
    for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)
      if (lista[j] > lista[j + 1]):
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
  
  return lista

if __name__ == "__main__":
  tamano_de_lista = int(input('De qué tamano será la lista? '))

  lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

  lista = ordenamiento_burbuja(lista)
  print(lista)
  print(lista)