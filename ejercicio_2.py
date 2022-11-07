# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt




    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    

    # Su implementación ya está disponible, es la siguiente:
def line_plot():
    x = list(np.linspace(-4, 4, 20))
    y1 = []
    for i in x:
       # y1 = x**2
        y1.append(i**2)

    y2 = []
    for i in x:
      #  y2 = x**3
        y2.append(i**3)

    fig = plt.figure()
    fig.suptitle('Y1=X**2 and Y2=X**3')
    ax = fig.add_subplot()

    ax.plot(x, y1, color= "blue", label='x cuadrado')
    ax.plot(x, y2, color= "red", label='x cubo')
    ax.legend()
    ax.grid()
    plt.show()

    # Alumno: Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    # Crear acá su gráfico
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")
    line_plot()
    print("terminamos")
