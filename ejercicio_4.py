# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt




    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
def multigrafico_plot():    
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    #y1 = x**2
    #y2 = x**3
    #y3 = x**4
    #y4 = np.sqrt(x)
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    for i in x:
        y1.append(i**2)
        y2.append(i**3)
        y3.append(i**4)
        raiz = (np.sqrt(i))
        y4.append(raiz)
    fig = plt.figure()
    fig.suptitle('Funciones de X', fontsize=16)
    ax1 = fig.add_subplot(2, 2, 1)  # 1 fila, 2 columnas, axes nº1
    ax2 = fig.add_subplot(2, 2, 2)  # 1 fila, 2 columnas, axes nº2
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    ax1.plot(x, y1, c='blue', label="Y = X cuadrada", marker= "+")
    ax1.set_title("Y=X Cuadrada")
    ax1.legend()
    ax1.grid()

 
    ax2.plot(x, y2, c='red', label="Y = X cubo", marker= "*")
    ax2.set_title("Y=X Cubo")
    ax2.legend()
    ax2.grid()

    ax3.plot(x, y3, c='green', label="Y = X cuarta", marker= ">")
    ax3.set_title("Y=X Cuarta")
    ax3.legend()
    ax3.grid()

    ax4.plot(x, y4, c='pink', label="Y = X raiz cuadrada", marker= "<")
    ax4.set_title("Y=X Raiz Cuadrada")
    ax4.legend()
    ax4.grid()

    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    plt.show()
    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")
    multigrafico_plot()
    print("terminamos")
