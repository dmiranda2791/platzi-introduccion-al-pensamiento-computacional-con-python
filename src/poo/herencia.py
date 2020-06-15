class Escuela:
  def __init__(self, nombre):
      self._nombre = nombre
      self.alumnos = []
  
  @property
  def nombre(self):
    return self._nombre

  @nombre.setter
  def nombre(self, nombre):
    self._nombre = nombre
  
  def matricular_alumno(self, nombre_alumno):
      self.alumnos.append(nombre_alumno)
  

class EscuelaPrivada(Escuela):
  def __init__(self, nombre, costo_matricula, costo_mensualidad):
    super().__init__(nombre)
    self.costo_matricula = costo_matricula
    self.costo_mensualidad = costo_mensualidad

  def pagar_matricula(self, cantidad):
    if (cantidad < self.costo_matricula):
      raise Exception('La cantidad no es suficiente para cubrir la matricula.')

  def pagar_mensualidad(self, cantidad):
    if (cantidad < self.costo_mensualidad):
        raise Exception('La cantidad recibida no es suficiente para cubrir el costo de la mensualidad.')
  
  def matricular_alumno(self, nombre_alumno, pago_matricula):
    self.pagar_matricula(pago_matricula)
    super().matricular_alumno(nombre_alumno)
  
class CasillaDeVotacion:
  def __init__(self, identificador, pais):
    self._identificado = identificador
    self._pais = pais
    self._region = None

  @property
  def region(self):
    return self._region

  @region.setter
  def region(self, region):
    if region in self._pais:
      self._region = region
    else:
      raise ValueError(f'La region {region} no est valida en (self._pais')

if __name__ == '__main__':
  escuela_wis = EscuelaPrivada('WIS', 7000, 3600)
  print(f'Nombre de la escuela: {escuela_wis.nombre}')
  escuela_wis.nombre = 'Western International School'
  print(f'Nombre de la escuela: {escuela_wis.nombre}')
  escuela_wis.matricular_alumno('Daniela Mirnada', 7000)
  escuela_wis.pagar_mensualidad(4000)


""" if __name__ == '__main__':
  casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])
  print(f'casilla.region={casilla.region}')
  casilla.region = 'Morelos'
  print(f'casilla.region={casilla.region}') """
  