# Algoritmo que realice el cifrado de un mensaje por permutación de filas, teniendo como clave n filas.
# Tanto n como el texto del mensaje se ingresan al iniciar el algoritmo. El algoritmo debe controlar que
# el número de caracteres del mensaje (sin espacios), sea menor o igual que n x n. Imprima la matriz de
# cifrado, el mensaje original y el mensaje cifrado. Si en la matriz de cifrado sobran espacios para almacenar
# los caracteres del mensaje original, estos deben llenarse con "*".

import time

# Ingreso de datos
mensaje = input("Ingresa el mensaje a cifrar: ")
n = int(input("Ingresa el número de filas: "))

# Eliminar espacios
mensaje_sin_espacios = mensaje.replace(" ", "")

# Comprobar si el mensaje cabe en la matriz
if len(mensaje_sin_espacios) > n * n:
    print(f"Error: el número de caracteres del mensaje es mayor a {n * n} caracteres (n x n).")
else:
    # Completar el mensaje con '*' si es necesario
    mensaje_sin_espacios += "*" * (n * n - len(mensaje_sin_espacios))

    # Crear la matriz de cifrado llenando verticalmente
    matriz_cifrado = [[''] * n for _ in range(n)]
    index = 0
    for col in range(n):
        for row in range(n):
            matriz_cifrado[row][col] = mensaje_sin_espacios[index]
            index += 1

    # Generar el mensaje cifrado tomando las filas de la matriz
    mensaje_c = ''.join(''.join(fila) for fila in matriz_cifrado)

    # Resultados
    print("Matriz de cifrado:")
    for fila in matriz_cifrado:
        print(fila)

    print("Mensaje original:", mensaje)
    print("Mensaje cifrado:", mensaje_c)

time.sleep(10)