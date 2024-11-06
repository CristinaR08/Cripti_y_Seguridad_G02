# Algoritmo que realice el cifrado de un mensaje por permutación de columnas, teniendo como clave n columnas.
# Tanto n como el texto del mensaje se ingresan al iniciar el algoritmo. El algoritmo debe controlar que el número de caracteres del
# mensaje (sin espacios), sea menor o igual que n x n. Imprima la matriz de cifrado, el mensaje original y el mensaje cifrado. 
# Si en la matriz de cifrado sobran espacios para almacenar los caracteres del mensaje original, estos deben llenarse con "*".

import numpy as np

def permutacion_columnas_numpy(mensaje, n):
    # Eliminamos los espacios y rellenamos con '*' si es necesario
    mensaje = mensaje.replace(" ", "")
    while len(mensaje) < n * n:
        mensaje += '*'

    # Convertimos el mensaje a una matriz de n x n usando NumPy
    matriz = np.array(list(mensaje)).reshape((n, n))

    # Imprimimos la matriz de cifrado
    print("Matriz de cifrado:")
    print(matriz)

    # Ciframos el mensaje leyendo por columnas
    mensaje_cifrado = ''
    for col in range(n):
        for fila in range(n):
            mensaje_cifrado += matriz[fila, col]  # Extraer cada elemento

    # Imprimimos el mensaje original y cifrado
    print("\nMensaje original:", mensaje)
    print("Mensaje cifrado:", mensaje_cifrado)


# Entrada de datos
n = int(input("Ingrese la clave (n columnas): "))
mensaje = input("Ingrese el mensaje: ")

# Ejecutamos el algoritmo con NumPy
permutacion_columnas_numpy(mensaje, n)
