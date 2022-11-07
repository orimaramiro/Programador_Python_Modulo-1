# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt

    # NOTA: aproveche los ejemplos de "line_plot" de clase

    # Se desea graficar los valores de "x" e "y" en un gráfico de línea
    # A continuación los datos ya disponibles de "x" e "y" para que utilice:
def line_plot():
    x = list(range(-10, 11, 1))
    # Bucle que completa y calcula todos los valores de "y"
    y = []
    for i in x:
        y.append(i**2)

    # Alumno: Crear una "figura" y crear un "ax" con add_subplot

    # Graficar el "line plot" de "y" en función de "x"
    fig = plt.figure()
    fig.suptitle('X vs Y = X**2', fontsize=14)
    ax = fig.add_subplot()
    ax.plot(x, y, color='green', label='Cuadrática')
    ax.legend()
    plt.show()
    # Alumno: Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección

    # Crear acá su gráfico

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")
    line_plot()
    print("terminamos")
