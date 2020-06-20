import random

def ordenamiento_por_insercion(lista): #O(n) * O(n) = O(n**2)
  n = len(lista)
  for final_lista_ordenada in range(1, n): #O(n)
    valor_actual = lista[final_lista_ordenada]
    indice_incersion = final_lista_ordenada

    while(indice_incersion > 0 and lista[indice_incersion - 1] > valor_actual): # O(n)
      lista[indice_incersion] = lista[indice_incersion - 1]
      indice_incersion -= 1

    lista[indice_incersion] = valor_actual
        
  return lista

if __name__ == "__main__":
  tamano_de_lista = 10#int(input('De qué tamano será la lista? '))

  lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

  print(lista)
  lista = ordenamiento_por_insercion(lista)
  print(lista)