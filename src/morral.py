
def morral(tamano_morral, pesos, valores, n):
  print(f'n={n}, tamano_morral={tamano_morral}, peso[n]={pesos[n - 1]}, valores[n - 1]={valores[n - 1]}')
  if tamano_morral == 0 or n == 0:
    return 0

  if (pesos[n - 1] > tamano_morral):
    return morral(tamano_morral, pesos, valores, n - 1)
  
  return max(
    valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1), 
    morral(tamano_morral, pesos, valores, n - 1)
  )

if (__name__ == '__main__'):
  pesos = [40, 65, 190, 80]
  valores = [30, 50, 70, 100]
  tamano_morral = 190
  n = len(pesos)

  resultado = morral(tamano_morral, pesos, valores, n)
  print(f'El resultado es {resultado}')

