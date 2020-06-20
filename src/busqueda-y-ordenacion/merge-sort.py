import random

def merge_sort(lista):
  if (len(lista) > 1):
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    i = 0
    j = 0
    k = 0
    while i < len(izquierda) and j < len(derecha):
      if (izquierda[i] < derecha[j]):
        lista[k] = izquierda[i]
        i += 1
      else:
        lista[k] = derecha[j]
        j += 1
      
      k += 1

    while (i < len(izquierda)):
      lista[k] = izquierda[i]
      k += 1
      i += 1
    
    while (j < len(derecha)):
      lista[k] = derecha[j]
      k += 1
      j += 1
      

  return lista




if __name__ == "__main__":
  tamano_de_lista = int(input('De qué tamano será la lista? '))

  lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

  print(lista)
  lista = merge_sort(lista)
  print(lista)