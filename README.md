
# Platzi - Curso de Introducción al Pensamiento Computacional con Python

Estos son los scripts de práctica durante el curso de Introducción al Pensamiento Computacional con Python de la plataforma Platzi. Se trata de scripts básicos cuyo objetivo es familiarze con algoritmos y la sintáxis báscia del lenguaje.

 Se utiliza un docker container como entorno de ejecución de los scripts.

## Pasos para ejecutar

### Prerequisitos
- Docker v19.03.4

1. Clonar el repositorio
```
git clone git@github.com:dmiranda2791/platzi-introduccion-al-pensamiento-computacional-con-python.git
```

2. Actualizar permisos de script de inicio.

Este script contiene un comando para ejecutar un docker container Ubuntu el cuál tendrá instalado Python v3.7 y montará la carpeta src del repo en la dirección /src del container.

```
chmod 700 start.sh
```

3. Ejectuar el script de inicio
```
./start.sh
```

Al ejecutar el script se abrirá la terminal del container de forma interactiva. Desde aquí se pueden ejecutar los scripts de la siguiente forma.

```
python src/busqueda_binaria.py
```

python -m venv env
source env/bin/activate
pip install bokeh
pip freeze
deactivate