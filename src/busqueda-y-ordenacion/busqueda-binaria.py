
import random 
import sys


sys.setrecursionlimit(2000)
def busqueda_binaria(lista, comienzo, final, objetivo):
  print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
  if(comienzo > final):
    return False

  medio = (comienzo + final) // 2

  if (lista[medio] == objetivo):
    return True
  elif(lista[medio] < objetivo):
    return busqueda_binaria(lista, medio + 1, len(lista), objetivo)
  else:
    return busqueda_binaria(lista, 0, medio - 1, objetivo)

if __name__ == "__main__":
  tamano_de_lista = int(input('De qué tamano será la lista? '))
  objetivo = int(input('Qué número quieres encontrar? '))

  lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])
  encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
  print(lista)
  print(f'El element {objetivo} {"esta" if encontrado else "no esta"} en la lista')