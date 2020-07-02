from bokeh import figure, output_file, show 
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource

def plot_linea():
  fig = figure()

  total_vals = int(input('Cuánto valores quieres graficar? '))
  x_vals = list(range(total_vals))

  y_vals = []

  for i in x_vals:
    val = int(input(f'Valor y para {i}: '))
    y_vals.append(val)

  fig.line(x_vals, y_vals, line_width=2)
  show(fig)

def plot_bar_chart():
  fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
  counts = [5, 4, 3, 6, 1, 9]

  source = ColumnDataSource(data=dict(fruits = fruits, counts=counts, color=Spectral6))

  fig = figure(x_range=fruits, y_range=(0, 12), plot_height = 550, title="Fruit Counts",
              toolbar_location=None, tools="")

  fig.vbar(x='fruits', top='counts', width=0.9, color='color', legend_field='fruits', source=source)
  fig.xgrid.grid_line_color = None
  fig.legend.orientation = 'horizontal'
  fig.legend.location = "top_center"

  show(fig)
if __name__ == '__main__':
  output_file('graficado_simple.html')
  plot_bar_chart()
