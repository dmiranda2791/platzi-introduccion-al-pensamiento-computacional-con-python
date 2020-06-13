class Coordenada:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distancia(self, otra_coordenada):
    x_diff = (self.x - otra_coordenada.x)**2
    y_diff = (self.y - otra_coordenada.y)**2

    return (x_diff + y_diff)**0.5

if __name__ == '__main__':
  coord_1 = Coordenada(3, 30)
  coord_2 = Coordenada(4, 8)

  print(f'Listancia entre coord_1 y coord_2 es {coord_1.distancia(coord_2)}')
  print(f'coord_1 isinstance de Coordenada: {isinstance(coord_1, Coordenada)}')